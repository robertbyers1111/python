#!/usr/bin/env python3

r"""
 +~~~~~~~~~~~~~~~~+
 | prune_json.py  |
 | Robert Byers   |
 | (c) 2020       |
 +~~~~~~~~~~~~~~~~+

INTRODUCTION: This script finds match strings in a JSON file, writing the matched strings to
stdout. The name of the JSON file (optionally including relative or absolute path) as well as
the match strings are specified as command-line arguments.

REQUIREMENTS:

    cpython3.6+ is the minimum python environment officially supported. Has been tested against python3.8.
    NOTE: Versions of python prior to 3.6 will definitely FAIL because f-strings, new in 3.6, are used extensively.

USAGE:

    python prune_json.py file match_strings ...

    where..

    file               Path to a JSON file
    match_strings      A space-separated list of strings to be found in the JSON file

EXIT STATUS:

    Exit status is set to 1 if no match was found, and set to 0 otherwise.

EXAMPLE:

    $ cat example.json
    {"ant": "bat", "cat": "dog", "elk": ["fox", "gnu", "hen"]}
    
    $ python3.7 prune_json.py example.json dog gnu hen
    {
        "cat": "dog",
        "elk": [
            "gnu",
            "hen"
        ]
    }
    
    $ echo $?
    0

LIMITATIONS:

    This script operates on any valid JSON, nested up to a depth of no more than 500.

    The following exceptions are NOT handled...

    o Missing input files
    o Input files containing invalid JSON
    o Any improper or malicious use of this script is not guarded against

"""

import json
import re
import sys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set up logging

import logging
#ogging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('prune_json')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Output_Buffer class
#
# This class contains a buffer which accumulates lines to be printed
# and lines that *might* need to be printed (depending on whether any
# children need to be printed)
#
# The functions in this class do not determine whether a line is to be
# printed or not. That intelligence is in a recursion function found 
# outside the scope of this class. The functions in the class are merely
# for storing and manipulating the json data while it is being processed, as
# well as for printing the buffer once the processing phase is complete.
#
# Each line has an attribute (should_print) indicating whether the line
# should be printed or not (true or false)
#
# A json value that is a string or an arrary will have its should_print
# attribute set immediately upon discovery. Such objects will not require
# updation of their should_print attribute thereafter.
#
# However, a json 'node' (i.e., a json object that contains one or more
# objects) starts off with its should_print attribute set to false. But
# this might be changed to true if any of its children are found to require
# printing. The class method 'update_should_print' is called to update the
# should_print attribute for nodes that are found to have children requiring
# printing.
#
# After processing the intput json file the output buffer will be mostly
# ready for printing, with just indentation and commas needing to be
# accounted for. The class function 'print' takes care of this.

class Output_Buffer():

    def __init__(self):
        self.buffer = []
        self.index = -1
        self.spaces = 4

    # Append a new JSON line to the buffer
    #
    #   line: (str) the JSON line to be written to the buffer
    #   recursion_level: (int) the recursion level at which this line was discovered
    #   should_print: (bool) the should_print status at the time this funcion is called

    def append_line(self, line, recursion_level, should_print):
        self.buffer.append([line, recursion_level, should_print])
        self.index += 1
        indent = ' ' * self.spaces * recursion_level
        logger.debug(indent + f"Appending line {line} to output buffer, recursion_level {recursion_level}, should_print {should_print}, index {self.index}")
        return self.index

    # Modify the should_print attribute for a particular JSON line
    #
    #   update_index: (int) the index into the buffer of the line to be updated
    #   should_print: (bool) the should_print status at the time this funcion is called

    def update_should_print(self, update_index, new_should_print):
        line, recursion_level, orig_should_print = self.buffer[update_index]
        self.buffer[update_index] = [line, recursion_level, new_should_print]
        indent = ' ' * self.spaces * recursion_level
        logger.debug(indent + f"Updating line at index {update_index} with new should_print value {new_should_print}")
        logger.debug(indent + f"Buffer at index {update_index} is now {self.buffer[update_index]}")

    # Add a trailing comma to a line depending on the JSON context at which this line exists.
    #
    #   Essentially, if the following line is a simply JSON key,value at the same
    #   level, a comma will be appended.
    #
    #   curr_index: (int) the index into the buffer of the line to be commafied

    def check_if_need_comma(self, curr_index):
        comma = ""
        if (curr_index < len(self.buffer)-1):
            curr_line, curr_recursion_level, curr_should_print = self.buffer[curr_index]

            #Find the next *printable* line

            max_index = len(self.buffer)
            next_line = ""
            next_should_print = False
            next_index=curr_index+1
            while not next_should_print and next_index < max_index:
                next_line, next_recursion_level, next_should_print = self.buffer[next_index]
                next_index += 1

            # Maybe there's nothing to print after current line
            if next_line == "":
                comma = ""

            # Or maybe current line already has a comma
            elif re.search(',\s*$', curr_line):
                comma = ""

            # Or maybe current line ends in a left curly brace
            elif re.search('{\s*$', curr_line):
                comma = ""

            # Or maybe next line is nothing but a right curly brace
            elif re.search('^\s*}\s*$', curr_line):
                comma = ""

            # Otherwise, we need a comma if next line starts with a quote
            elif re.search('\s*\"', next_line):
                comma = ","

        return comma

    # Print the output buffer.
    #
    #     Print any JSON line from the output buffer with its should_print attribute
    #     set to true. Indentation is handled here, as well as displaying the root level
    #     enclosing '{' and '}'

    def print(self):
        lines_printed = 0
        max_index = len(self.buffer)
        if max_index > 0:
            for curr_index in range(0,max_index):
                line, recursion_level, should_print = self.buffer[curr_index]
                if should_print:
                    comma = self.check_if_need_comma(curr_index)
                    if lines_printed == 0:
                        print("{")
                    lines_printed += 1
                    print(f"{' ' * self.spaces * recursion_level}{line}{comma}")
            if lines_printed != 0:
                print("}")

        if lines_printed > 0:
            print("") # display a final line per specification
            anything_found = True
        else:
            anything_found = False

        return anything_found

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# recurse_into()
#
# This recursive function is called each time a new JSON object (stored as
# a dict in python) is discovered. 
#
# If the new object contains any basic JSON object (a string value or an
# array value) that match one of the match strings, then the basic object
# is appended to the output buffer (should_print attribute set to True).
#
# A crucial step here is that the should_print attribute is *returned*
# to the calling recursion level. This is how a positive should_print 
# attribute percolates its status up to its parents.
#
# Each parent finding a should_print return value enabled will then
# update its own should_print attribute.

def recurse_into(recursion_level, obj, match_strings):

    # This is for logging indentation
    spaces_per_level = 4
    indent = " " * recursion_level * spaces_per_level

    logger.debug("")
    logger.debug(indent + "~"*40)
    logger.debug(indent + f"Commence recursion level {recursion_level}")

    should_print_any = False

    # JSON 'nodes' (objects containing further objects) were converted
    # to dicts when json.load() was called.

    if type(obj) is dict:
        for key, value in obj.items():

            should_print = False

            logger.debug("")
            logger.debug(indent + "Checking key,value..")
            logger.debug(indent + f"key: {key}, type: {type(key)}")
            logger.debug(indent + f"value: {value}, type: {type(value)}")
            logger.debug(indent + f"should_print is {should_print}")
            logger.debug(indent + f"should_print_any is {should_print_any}")

            # A simple JSON value can be tagged for printing as soon as we see it

            if type(value) is str:
                for match_string in match_strings:
                    logger.debug(indent + f"Check if {match_string} is {value}")
                    if match_string == value:
                        should_print, should_print_any = True, True
                        logger.debug(indent + f"MATCH FOUND! (string) ............ {recursion_level}, {key}, {match_string}, {should_print}, {should_print_any}")
                        output_buffer.append_line(f'"{key}" : "{value}"', recursion_level, should_print)
                        logger.debug(indent + f"Just appended key {key} : {value} to output buffer, should_print {should_print}, should_print_any {should_print_any}")
                        break

            # A JSON array can also be tagged for printing as soon as we see it

            elif type(value) is list:
                for match_string in match_strings:
                    logger.debug(indent + f"Check if {match_string} is in {value}")
                    if match_string in value:
                        should_print, should_print_any = True, True
                        logger.debug(indent + f"MATCH FOUND! (list) ............ {recursion_level}, {key}, {match_string}, {should_print}, {should_print_any}")
                        output_buffer.append_line(f'"{key}" : "{value}"', recursion_level, should_print)
                        logger.debug(indent + f"Just appended key {key} : {value} to output buffer, should_print {should_print}, should_print_any {should_print_any}")
                        break

            # Finding a new JSON object means we append its name to the output buffer,
            # but set its should_print to False. We then update should_print later if
            # any children had their should_print set to True

            elif type(value) is dict:
                index = output_buffer.append_line(f'"{key}" : {{', recursion_level, should_print)
                logger.debug(indent + f"Just appended key {key} to output buffer, should_print {should_print}. Buffer index is {index}")
                should_print = recurse_into(recursion_level+1, value, match_strings)
                logger.debug(indent + f"Returned to level {recursion_level}, key {key}, should_print is {should_print}, should_print_any is {should_print_any}")
                if should_print:
                    logger.debug(indent + f"Updating should_print for level {recursion_level}, key {key}")
                    output_buffer.update_should_print(index, should_print)
                    output_buffer.append_line('}', recursion_level, should_print)
               #elif should_print_any:
               #    output_buffer.update_should_print(index, should_print_any)
               #    output_buffer.append_line('}', recursion_level, should_print_any)

            else:
                logger.error(indent + f"Unexcpected value type ({type(value)}) in recurse_into")
    else:
        logger.error(indent + "Unexcpected object type ({type(obj)}) in recurse_into")

    logger.debug(indent + f"Leaving level {recursion_level}, key {key}, should_print {should_print}, should_print_any {should_print_any}")
    logger.debug(indent + "~"*40)
    logger.debug("")
    return should_print or should_print_any

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():

    # COMMAND LINE PROCESSING
    # First arg is path to the JSON input file
    # Additional args are the match strings

    input_json_filename = sys.argv[1]
    match_strings = sys.argv[2:]

    logger.debug(f'input_json_filename: {input_json_filename}')
    logger.debug(f'match_strings: {match_strings} ({type(match_strings)})')

    infile = open(input_json_filename,'r')

    # START OF LOADING, ANALYZING AND PRINTING PHASES

    with infile:
        try:
            # LOADING PHASE (read the json file into memory)

            objs = (json.load(infile),)
            logger.debug(f"There are {len(objs)} objects at the root level")

            # ANALYZING PHASE

            for obj in objs:
                if type(obj) is dict:
                    should_print = recurse_into(1, obj, match_strings)
                else:
                    logger.error(f"Unexcpected object type ({type(obj)}) in main")

            # PRINTING PHASE

            anything_found = output_buffer.print()

            if anything_found:
                exit_status = 0
            else:
                exit_status = 1

        except ValueError as e:
            raise SystemExit(e)

    return exit_status

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    output_buffer = Output_Buffer()
    exit_status = main()
    sys.exit(exit_status)
