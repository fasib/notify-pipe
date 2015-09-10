#!/usr/bin/env python
import sys
from gi.repository import Notify
from argparse import ArgumentParser

def _main():
	parser = ArgumentParser()
	parser.add_argument(
		'-n','--name', help='name', default="notify-pipe")
	parser.add_argument(
		'-i','--icon', help='icon ', default="")

	args = parser.parse_args()

	Notify.init("notify-pipe")

	name = args.name

	Hello = Notify.Notification.new (name)
	Hello.show()

	lines_iterator = iter(sys.stdin.readline, b"")
	for line in lines_iterator:
		print(line.decode()),
		sys.stdout.flush()
		Hello.update(name, line, args.icon)
		Hello.show()

if __name__ == '__main__':
	try:
		_main()
	except KeyboardInterrupt:
		sys.exit(0)
