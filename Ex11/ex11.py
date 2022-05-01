###############################################################################
# FILE : ex11.py
# WRITER : shay kvasha , shayk96 , 207902602
# EXERCISE : intro2cse ex11 2020
# DESCRIPTION: a little program that builds a tree and diagnose illnesses
###############################################################################
from collections import Counter
from itertools import combinations

MIN_SUCCESS_RATE = 0
TEMPORARY_NAME = 'temp'


class Node:
	"""
	the class creates a tree object
	"""
	def __init__(self, data, positive_child=None, negative_child=None):
		"""
		the main constructor for the class. builds the tree
		:param data: the name of the node
		:param positive_child: the node negative child
		:param negative_child: the nose positive child
		"""
		self.data = data
		self.positive_child = positive_child
		self.negative_child = negative_child


class Record:
	"""
	the class constructs an object that consists of an illness and its symptoms
	"""
	def __init__(self, illness, symptoms):
		"""
		the main constructor for the class. constructs the objects
		:param illness: the name of the illness
		:param symptoms: the illness symptoms
		"""
		self.illness = illness
		self.symptoms = symptoms

	def get_illness(self):
		"""
		returns the illness name
		:return: the illness name
		"""
		return self.illness

	def get_symptoms(self):
		"""
		returns the illness symptoms
		:return: the illness symptoms
		"""
		return self.symptoms


def parse_data(filepath):
	"""
	reads the txt file provided and cals the Records class to construct objects
	from the data
	:param filepath: the file to be read
	:return: objects of class records type
	"""
	with open(filepath) as data_file:
		records = []
		for line in data_file:
			words = line.strip().split()
			records.append(Record(words[0], words[1:]))
		return records


class Diagnoser:
	"""
	the class gets a tree and checks the tree for different things
	"""
	def __init__(self, root):
		"""
		creates an object from a tree given
		:param root: the tree
		"""
		self.root = root

	def diagnose(self, symptoms):
		"""
		receives a list of symptoms "and diagnoses" which disease is suitable
		for them according to the decision tree kept in self
		:param symptoms: a list of symptoms
		:return:
		"""
		return self.diagnose_helper(self.root, symptoms)

	def diagnose_helper(self, cur, symptoms):
		"""
		a recursive method that goes through the tree until it reaches the
		final node(leaf) and returns the data of it
		:param cur: the current node
		:param symptoms: a list of symptoms
		:return: the final node(leaf)
		"""
		if cur.positive_child is None and cur.negative_child is None:
			return cur.data
		if cur.data in symptoms:
			return self.diagnose_helper(cur.positive_child, symptoms)
		else:
			return self.diagnose_helper(cur.negative_child, symptoms)

	def calculate_success_rate(self, records):
		"""
		the method checks the success rate of the given tree in comparison to
		all the records given
		:param records: a list of records
		:return: a float indicating the success rate
		"""
		counter = 0
		for i in records:
			if self.diagnose(i.get_symptoms()) == i.get_illness():
				counter += 1
		success_rate = counter / len(records)
		return success_rate

	def all_illnesses(self):
		"""
		goes through the tree and returns all the illness in
		it (the leaves data)
		:return: the illness on the tree in order of most common to
		least common
		"""
		not_sorted = self.all_illnesses_helper(self.root, {})
		return sorted(not_sorted, key=not_sorted.get, reverse=True)

	def all_illnesses_helper(self, cur, illnesses_dic):
		"""
		a recursive method that goes through the tree and count the leaves data
		:param cur: the current node
		:param illnesses_dic: a dictionary containing key and value. the keys
		are the illness name and the value are the number of times it appears
		in the tree
		:return: a dictionary sustained of illnesses and the number of
		occurrences
		"""
		if cur.positive_child is None and cur.negative_child is None:
			if cur.data in illnesses_dic:
				illnesses_dic[cur.data] += 1
			else:
				illnesses_dic[cur.data] = 1
			return illnesses_dic
		if cur.positive_child is not None:
			self.all_illnesses_helper(cur.positive_child, illnesses_dic)
		if cur.negative_child is not None:
			self.all_illnesses_helper(cur.negative_child, illnesses_dic)
		return illnesses_dic

	def paths_to_illness(self, illness):
		"""
		goes through all the routes in the tree and return a list of all the
		routes that reach the leaf on which the illness is stored
		:param illness: the illness being searched for
		:return: a list containing all the paths to the illness(list of lists)
		"""
		path = []
		all_paths = []
		self.path_to_illness_helper(self.root, illness, path, all_paths)
		return all_paths

	def path_to_illness_helper(self, cur, illness, path, all_paths):
		"""
		a recursive method that goes through the tree and builds the paths
		to each leaf
		:param cur: the current node
		:param illness: the illness being searched for
		:param path: one path towards the illness
		:param all_paths: an empty list being filled with lists that contain
		the path to the illness
		:return: a list containing all the paths to the illness(list of lists)
		"""
		if cur.positive_child is None and cur.negative_child is None:
			if cur.data == illness:
				return all_paths.append(path)
			else:
				return
		if cur.positive_child is not None:
			self.path_to_illness_helper(cur.positive_child, illness,
										path + [True], all_paths)
		if cur.negative_child is not None:
			self.path_to_illness_helper(cur.negative_child, illness,
										path + [False], all_paths)


def build_tree(records, symptoms):
	"""
	builds a tree from the symptoms and records
	:param records: a list of objects from record class type
	:param symptoms: a list of symptoms
	:return: the root of the tree
	"""
	root = tree_helper(symptoms)
	lst_in = []
	lst_out = []
	leaves_data(records, root, lst_in, lst_out)
	return root


def tree_helper(symptoms):
	"""
	builds the tree from the symptoms and puts a temporary data in the leaves
	:param symptoms: a list of symptoms
	:return: a tree with temporary leaves
	"""
	if len(symptoms) == 0:
		return Node(TEMPORARY_NAME, None, None)
	return Node(symptoms[0], tree_helper(symptoms[1:]),
							tree_helper(symptoms[1:]))


def leaves_data(records, cur, lst_in, lst_out):
	"""
	puts illness names in the tree leaves according to the right path
	:param records: a list of objects from record class type
	:param cur: the current node
	:param lst_in: a lst of symptoms that are true for the illness
	:param lst_out: a lst of symptoms that are not true for the illness
	:return: a final tree
	"""
	if cur.positive_child is not None:
		leaves_data(records, cur.positive_child, lst_in + [cur.data], lst_out)
	if cur.negative_child is not None:
		leaves_data(records, cur.negative_child, lst_in, lst_out + [cur.data])
	else:
		cur.data = right_illness(records, lst_in, lst_out)


def right_illness(records, lst_in, lst_out):
	"""
	checks what is the right illness to put in each leaf
	:param records: a list of objects from record class type
	:param lst_in: a lst of symptoms that are true for the illness
	:param lst_out: a lst of symptoms that are not true for the illness
	:return: the right illness to put in the leaf
	"""
	illness = Counter()
	for record in records:
		for symptom in record.get_symptoms():
			if symptom in lst_out:
				break
		else:
			for symptom in lst_in:
				if symptom not in record.get_symptoms():
					break
			else:
				if record.get_illness() not in illness:
					illness[record.get_illness()] = 1
				else:
					illness[record.get_illness()] += 1
	if not illness:
		return None
	else:
		return illness.most_common(1)[0][0]


def optimal_tree(records, symptoms, depth):
	"""
	builds trees and checks which one is the one with best success rate
	:param records: a list of objects from record class type
	:param symptoms: a list of symptoms
	:param depth: number of symptoms to ask about
	:return: the tree with the best success rate
	"""
	optimal_tree_root = None
	possible_combo = combinations(symptoms, depth)
	min_success_rate = MIN_SUCCESS_RATE
	for combo in possible_combo:
		cur_root = build_tree(records, combo)
		cur_diagnoser = Diagnoser(cur_root)
		cur_error_rate = cur_diagnoser.calculate_success_rate(records)
		if cur_error_rate > min_success_rate:
			min_success_rate = cur_error_rate
			optimal_tree_root = cur_root
	return optimal_tree_root
