# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# Unit Tests
#

import copy

from UnitaryTest.test_tools import TestTools
from ex42_gaming_social_network import *

NETWORK = [['John', ['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 
	['Bryant',['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 
	['Mercedes', ['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 
	['Olive', ['John', 'Ollie'],['The Legend of Corgi', 'Starfleet Commander']], 
	['Debra', ['Walter', 'Levi', 'Jennie', 'Robin'], ['Seven Schemers', 'Pirates in Java Island', 'Dwarves and Swords']], 
	['Walter', ['John', 'Levi', 'Bryant'], ['Seahorse Adventures', 'Ninja Hamsters', 'Super Mushroom Man']], 
	['Levi', ['Ollie', 'John', 'Walter'], ['The Legend of Corgi', 'Seven Schemers', 'City Comptroller: The Fiscal Dilemma']], 
	['Ollie', ['Mercedes', 'Freda', 'Bryant'], ['Call of Arms', 'Dwarves and Swords', 'The Movie: The Game']], 
	['Jennie', ['Levi', 'John', 'Freda', 'Robin'], ['Super Mushroom Man', 'Dinosaur Diner', 'Call of Arms']], 
	['Robin', ['Ollie'], ['Callof Arms', 'Dwarves and Swords']], 
	['Freda', ['Olive', 'John', 'Debra'], ['Starfleet Commander', 'Ninja Hamsters', 'Seahorse Adventures']]]

def create_data_structure_ut():
	t = TestTools()

	# Test parse_info for contacts
	t_input = 'John is connected to Bryant, Debra, Walter'
	exp = ['John', ['Bryant', 'Debra', 'Walter']]
	t.new_test(func=parse_info)
	t.evaluate_result(parse_info(t_input, CONNECTION_STR), expected=exp)

	# Test parse_info for likes
	t_input = 'John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner'
	exp = ['John', ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']]
	t.new_test(func=parse_info)
	t.evaluate_result(parse_info(t_input, LIKES_STR), expected=exp)

	# Test find_user_bucket(network, user)
	network = [['John', ['Bryant', 'Debra', 'Walter']], ['Bryant', ['Olive', 'Ollie', 'Freda', 'Mercedes']]]
	t.new_test(func=find_user_bucket)
	t.evaluate_result(find_user_bucket(network, 'John'), expected=['John', ['Bryant', 'Debra', 'Walter']])

	t.new_test(func=find_user_bucket)
	t.evaluate_result(find_user_bucket(network, 'Ollie'), expected=None)

	# Test create_data_structure
	example_input_short = "John is connected to Bryant, Debra, Walter.\
	John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
	Bryant is connected to Olive, Ollie, Freda, Mercedes.\
	Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
	Mercedes is connected to Walter, Robin, Bryant.\
	Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
	Olive is connected to John, Ollie.\
	Olive likes to play The Legend of Corgi, Starfleet Commander."

	example_output = [['John', ['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 
					 ['Bryant', ['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 
					 ['Mercedes', ['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 
					 ['Olive', ['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']]] 
	
	t.new_test(func=create_data_structure)
	t.evaluate_result(create_data_structure(example_input_short), expected=example_output)

def get_connections_ut():
	t = TestTools()
	
	# Test get_connections
	network = [['John', ['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 
					 ['Bryant', ['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 
					 ['Mercedes', ['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 
					 ['Olive', ['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']], ['Ollie',['likes']], ['Phil',[],[]]] 
	
	t.new_test(func=get_connections)
	t.evaluate_result(get_connections(network, 'Bryant'), expected=['Olive', 'Ollie', 'Freda', 'Mercedes'])

	t.new_test(func=get_connections)
	t.evaluate_result(get_connections(network, 'Frida'), expected=None)

	t.new_test(func=get_connections)
	t.evaluate_result(get_connections(network, 'Ollie'), expected=[])

def get_games_liked_ut():
	t = TestTools()

	# Test get_bucket_info(bucket, idx)
	l = ['John', ['Ollie', 'Walter'], ['The Game']]
	t.new_test(func=get_bucket_info)
	t.evaluate_result(get_bucket_info(l, CONNECTIONS_POS_IN_BUCKET), expected=['Ollie', 'Walter'])

	t.new_test(func=get_bucket_info)
	t.evaluate_result(get_bucket_info(l, LIKES_POS_IN_BUCKET), expected=['The Game'])

	# Test get_games_liked	
	network = [['John', ['Bryant', 'Debra', 'Walter'], ['The Movie: The Game', 'The Legend of Corgi', 'Dinosaur Diner']], 
				['Bryant', ['Olive', 'Ollie', 'Freda', 'Mercedes'], ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']], 
				['Mercedes', ['Walter', 'Robin', 'Bryant'], ['The Legend of Corgi', 'Pirates in Java Island', 'Seahorse Adventures']], 
				['Olive', ['John', 'Ollie'], ['The Legend of Corgi', 'Starfleet Commander']], ['Ollie',['likes']], ['Phil',[],[]]] 

	t.new_test(func=get_games_liked)
	t.evaluate_result(get_games_liked(network, 'Olive'), expected=['The Legend of Corgi', 'Starfleet Commander'])

	t.new_test(func=get_games_liked)
	t.evaluate_result(get_games_liked(network, 'Frida'), expected=None)

	t.new_test(func=get_games_liked)
	t.evaluate_result(get_games_liked(network, 'Phil'), expected=[])

def add_connection_ut():
	t = TestTools()
	
	# Test add_connection(network, user_A, user_B)
	OLIVE_POSITION_IN_TEST_NETWORK = 3
	network_updated = copy.deepcopy(NETWORK)
	network_updated[OLIVE_POSITION_IN_TEST_NETWORK][CONNECTIONS_POS_IN_BUCKET].append('Robin')

	t.new_test(func=add_connection)
	t.evaluate_result(add_connection(NETWORK, 'John', 'Walter'), expected=NETWORK)

	t.new_test(func=add_connection)
	t.evaluate_result(add_connection(NETWORK, 'Olive', 'Robin'), expected=network_updated)

	t.new_test(func=add_connection)
	t.evaluate_result(add_connection(NETWORK, 'Johnny', 'Mercedes'), expected=False)

# Test add_new_user
def add_new_user_ut():
	t = TestTools()

	new_user_games = ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
	bryant_games = ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']
	new_user_data = ['Smith', [], ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']] 
	
	network_updated = copy.deepcopy(NETWORK)
	network_updated.append(new_user_data)

	t.new_test(func=add_new_user)
	t.evaluate_result(add_new_user(NETWORK, 'Smith', new_user_games), expected=network_updated)

	t.new_test(func=add_new_user)
	t.evaluate_result(add_new_user(NETWORK, 'Bryant', bryant_games), expected=NETWORK)

# Test get_secondary_connections(network, connections)
def get_secondary_connections_ut():
	t = TestTools()

	exp = ['Olive', 'Ollie', 'Freda', 'Mercedes', 'Walter', 'Levi', 'Jennie', 'Robin', 'John', 'Bryant']
	t.new_test(func=secondary_connections)
	t.evaluate_result(secondary_connections(NETWORK, ['Bryant', 'Debra', 'Walter']), expected=exp)

	t.new_test(func=get_secondary_connections)
	t.evaluate_result(get_secondary_connections(NETWORK, 'John'), expected=exp)

# Test count_common_connections(network, user_A, user_B)
def count_common_connections_ut():
	t = TestTools()

	t.new_test(func=count_common_connections)
	t.evaluate_result(count_common_connections(NETWORK, 'John', 'Jennie'), expected=0)

	t.new_test(func=count_common_connections)
	t.evaluate_result(count_common_connections(NETWORK, 'John', 'Mercedes'), expected=2)

	t.new_test(func=count_common_connections)
	t.evaluate_result(count_common_connections(NETWORK, 'John', 'Freda'), expected=1)


# Test find_path_to_friend(network, user_A, user_B)
def find_path_to_friend_ut():
	t = TestTools()

	network = [['Abe',['Gel'],[]], 
			   ['Sam',['Zed'],[]], 
			   ['Gel',['Sam'],[]],
			   ['Zed',['Cho'],[]]]

	t.new_test(func=find_path_to_friend)
	t.evaluate_result(find_path_to_friend(network, 'Abe', 'Gel'), expected=['Abe', 'Gel'])

	t.new_test(func=find_path_to_friend)
	t.evaluate_result(find_path_to_friend(network, 'Abe', 'Sam'), expected=['Abe', 'Gel', 'Sam'])

	t.new_test(func=find_path_to_friend)
	t.evaluate_result(find_path_to_friend(network, 'Abe', 'Zed'), expected=['Abe', 'Gel', 'Sam', 'Zed'])

	t.new_test(func=find_path_to_friend)
	t.evaluate_result(find_path_to_friend(network, 'Abe', 'Cho'), expected=['Abe', 'Gel', 'Sam', 'Zed', 'Cho'])

	t.new_test(func=find_path_to_friend)
	t.evaluate_result(find_path_to_friend(network, 'Abe', 'Day'), expected=None)



if __name__ == '__main__':
	# create_data_structure_ut()
	# get_connections_ut()
	# get_games_liked_ut()
	# add_connection_ut()
	# add_new_user_ut()
	# get_secondary_connections_ut()
	# count_common_connections_ut()
	find_path_to_friend_ut()
