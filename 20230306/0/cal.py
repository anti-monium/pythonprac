import cmd
import shlex
from calendar import TextCalendar as tc 

class Cal(cmd.Cmd):
    prompt = "calendar"
    
    def do_month(self, arg):
        """month [theyear, themonth, w=0, l=0] -- Print a month’s calendar"""
        args = arg.split()
        tc.prmonth(int(args[1]), int(args[2]), w=int(args[3]), l=int(args[4]))
        
    def do_year(self, arg):
        """year [theyear, w=2, l=1, c=6, m=3] -- Print the calendar for an entire year"""
        args = arg.split()
        tc.pryear(int(args[1]), w=int(args[2]), l=int(args[3]), c=int(args[4]), m=int(args[5]))
        
    def complete_echo(self, prefix, line, start, end):
        variants = "month", "year"
        self.dump = prefix, line, start, end
        return [s for s in variants if s.startswith(prefix)]
        
    def do_quit(self, arg):
        """Quit programm"""
        
    def do_EOF(elf, arg):
        return 1
        
    
Cal().cmdloop()
