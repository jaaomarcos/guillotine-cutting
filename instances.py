class Instances(object):
	def __init__(self):
		self.files = []
		self.instances = dict()
	def process(self):
		for i in range(0, len(self.files)):
			file = open('instances/'+self.files[i]+'.txt').readlines()
			pecas = []
			for j in range(0, len(file)):
				valor =  file[j].split(' ')
				if j == 0:
					placa = [int(valor[0]), int(valor[1])]
				else:
					pecas.append([int(valor[0]), int(valor[1])])
			self.instances[i] = {'placa': placa, 'pecas': pecas}
			pass
		