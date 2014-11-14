__author__ = 'Alex Kim'


import re
import json
import unittest

in_list = ['R7A',
           'R8A',
           'C4-4A',
           'M3-2',
           'R8B',
           'C1-6A',
           'R7B',
           'R8X',
           'C1-7A',
           'PARK',
           'C1-9A',
           'R6',
           'C1-7',
           'C2-6',
           'R10',
           'C4-5',
           'C6-3X',
           'C1-6',
           'C6-2M',
           'C6-4M',
           'M2-4',
           'M1-5/R7X']

pat = re.compile(r"""
    (?P<General_Residence_Districts>
        ^R([1-9]|10)-([1-9]|10)$        # R1-1 to R10-10
        |
        ^R([1-9]|10)[A-H]$              # R1A to R10H
        )
    |(?P<Commercial_Districts>
        ^C1-[6-9]$                      # C1-6 to C1-9
        |
        ^C[2-7]-[0-9]$                  # C2-0 to C7-9
        |
        ^C8-[0-4]$                      # C8-0 to C8-4
        )
    |(?P<Manufacturing_Districts>
        ^M1-[1-9]$                      # M1-1 to M1-9
        |
        ^M2-[0-9]$                      # M2-0 to M2-9
        |
        ^M3-[0-2]$                      # M3-0 to M3-2
        )
    |(?P<Mixed_Manufacturing_And_Residential_Districts>
        ^M1-[1-6]/R([5-9]|10)$
        )
    |(?P<Battery_Park_City>
        ^BPC$)
    |(?P<New_York_City_Parks>
        ^PARK$)
    |(?P<New_York_State_Parks>
        ^PARKNYS$)
    |(?P<United_States_Parks>
        ^PARKUS$)
    |(?P<Zoning_Not_Applicable>
        ^ZNA$)
    |(?P<Special_Zoning_District>
        ^ZR\s(                           # Match "ZR "
          (1[1-9])                       # 11 to 19
          |
          ([2-9][0-9])                   # 20 to 99
          |
          (1[0-4][0-9])                  # 100 to 149
          |
          (15[0-1])                      # 150 to 151
         )$)
    |(?P<Not_Found>
        ^.*$)                            # Catch All
    """
                 , re.X)


def elem_to_match(pattern, elem):
    """
    :param pattern: All codes and their descriptions.
    :param elem: An individual code to find in the pattern.
    :return: The code and its description.
    """
    for desc, code in re.match(pattern, elem).groupdict().iteritems():
        if code:
            return {"code": code, "description": desc.replace('_', ' ')}


expected = {'codes': [{'code': 'R7A', 'description': 'General Residence Districts'},
                      {'code': 'R8A', 'description': 'General Residence Districts'},
                      {'code': 'C4-4A', 'description': 'Not Found'},
                      {'code': 'M3-2', 'description': 'Manufacturing Districts'},
                      {'code': 'R8B', 'description': 'General Residence Districts'},
                      {'code': 'C1-6A', 'description': 'Not Found'},
                      {'code': 'R7B', 'description': 'General Residence Districts'},
                      {'code': 'R8X', 'description': 'Not Found'},
                      {'code': 'C1-7A', 'description': 'Not Found'},
                      {'code': 'PARK', 'description': 'New York City Parks'},
                      {'code': 'C1-9A', 'description': 'Not Found'},
                      {'code': 'R6', 'description': 'Not Found'},
                      {'code': 'C1-7', 'description': 'Commercial Districts'},
                      {'code': 'C2-6', 'description': 'Commercial Districts'},
                      {'code': 'R10', 'description': 'Not Found'},
                      {'code': 'C4-5', 'description': 'Commercial Districts'},
                      {'code': 'C6-3X', 'description': 'Not Found'},
                      {'code': 'C1-6', 'description': 'Commercial Districts'},
                      {'code': 'C6-2M', 'description': 'Not Found'},
                      {'code': 'C6-4M', 'description': 'Not Found'},
                      {'code': 'M2-4', 'description': 'Manufacturing Districts'},
                      {'code': 'M1-5/R7X', 'description': 'Not Found'}]}


class TestPattern(unittest.TestCase):

    def test_example(self):
        result = json.dumps({'codes': [elem_to_match(pat, v) for v in in_list]}, indent=4)
        self.assertEqual(result, json.dumps(expected, indent=4), 'Code Lookup Failed')


if __name__ == '__main__':
    unittest.main()