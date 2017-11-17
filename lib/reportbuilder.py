#!/usr/bin/env python3
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** lib/reportbuilder.py      Report Generator        VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

class report_builder:
    @classmethod
    def __init__(self):
        """initialising report generator"""
        self.reportdata: dict = []
        self.valid_subjects: list = ["purged_files"]

    @classmethod
    def update(self, kwargs):
        """reportdata collector"""
        for key, value in kwargs:
            if key not in self.valid_subjects:
                raise TypeError("update recieved an unknown subject: \
                {}".format(key)
            else:
                field = self.reportdata[key]
                if type(field) == int or type(field) == float:
                    self.reportdata[key] =+ value
                else:
                    self.reportdata[key] = self.reportdata[key] + value

    @classmethod
    def render_report(self, reportType):
        """reportbuilder info, more to come"""
        ###TODO### devise a way to generate the report properly
        #if reportType == "display":
        #    print '### display template'
        #elif reportType == "html":
        #    print '### html template'
        #else:                        # reportType = "text"
        #    print '### text template'
        pass

def main():
    """just in case somebody wants to test this file by itself"""
    print("It works!!! ;-)")
    ###TODO### do something with the various methods/functions of this file

# standard boilerplate
if __name__ == '__main__':
    main()
