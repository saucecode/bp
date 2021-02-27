import sys, os, json

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Outputs a barebones source file in the desired language.')
	parser.add_argument('lang', metavar='lang', type=str, nargs=1, help='desired language')
	parser.add_argument('-n', dest='name', default={}, help='Boilerplate file name')

	args = parser.parse_args()

	lang = args.lang[0]
	
	template_file = f'templates/{lang}'
	
	if not os.path.exists(template_file):
		print('Unknown language', lang)
		sys.exit(0)
	
	json_data = None
	with open(template_file, 'r') as f:
		for line in f:
			
			if json_data is None:
				json_data = json.loads(line)
				continue
			
			line = line.replace('%%name%%', args.name or json_data.get('default_name') or '')
			print(line, end='')