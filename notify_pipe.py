#!/usr/bin/env python
import sys
from gi.repository import Notify
from argparse import ArgumentParser

def _main():
	parser = ArgumentParser()
	parser.add_argument(
		'-n','--name', help='name', default="notify-pipe")

	args = parser.parse_args()

	Notify.init("notify-pipe")

	name = args.name

	Hello = Notify.Notification.new (name)
	Hello.show()

	lines_iterator = iter(sys.stdin.readline, b"")
	for line in lines_iterator:
		print(line.decode()),
		Hello.update(name,line)
		Hello.show()

if __name__ == '__main__':
	_main()
