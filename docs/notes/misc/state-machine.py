# state that manages the options of the workflow 
# tells you the current workflow state, they will be 
# until they pick the right option

# root 
root_options = [
	"login", "sign-up"
]

option_children_for_login = [
	"view_items_to_deliver", 
	"view_products", 
	"add_products",
	"update_profile", 
	"logout"
]

option_children_for_product = [
	"next_page", "previous_page", "go_back"
]

while True:
	if state == login && self.authenticated_true: 
		# change the state 
		state = show_prompt_options(state, option_children_for_login)
	else if state == "view_items_to_deliver": 
		show_prompt_options() # of view items to deliver or 
		# you do something here


def show_prompt_options(state, options):
	for o in options: 
		print o 
	user_input = input()
	
	if user_input in options:
		return user_input
	
	return state