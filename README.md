Pexpect Fixture Runner
======================

Runner for simple pexpect test fixtures (created to test command line programs
by students learning C programming).  
Requires Pexpect: https://github.com/noahspurrier/pexpect.


Fixture syntax
--------------

One instruction per line. The following are valid instructions:

**<**  
Enter input to the program (pexpect.sendline).  
Ex.: < 1 + 1

**>**  
Expected output. You can use regular expressions here (pexpect.expect).  
Ex.: > .*

**!**  
Custom unexpected error message. Use after a > instruction.  
Ex.: ! Unexpected output!

**@**  
Breakpoint. Switch to interactive mode (pexpect.interact).  
Ex.: @

**#**  
Introduce a comment.  
Ex.: # This is a comment


Runner options
--------------

    usage: pexpect-fixture-runner.py [-h] [--verbose VERBOSITY_LEVEL] [--timeout TIMEOUT] command fixture

    Simple pexpect fixture runner.

    positional arguments:
    command               Command to run
    fixture               Path to fixture

    optional arguments:
    -h, --help            show this help message and exit
    --verbose VERBOSITY_LEVEL, -v VERBOSITY_LEVEL
                            Verbosity level; allowed values: 0 (default), 1, 2
    --timeout TIMEOUT, -t TIMEOUT
                            Expect timeout value (default: 2)


Example
-------

    [example.fx]
    # Python prompt
    > >>>
    # Hello world!
    < print 'Hello World!'
    > Hello World!
    # 1 + 1
    < 1 + 1
    > 2


Running the fixture above:


    $ pexpect-fixture-runner.py python example.fx
    SUCCESS
    -- Fixture completed, waiting process normal exit.
    ...killing still running process.
