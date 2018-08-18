# Test utils

total_run_tests = 0
num_success = 0

DIVIDER_LEN = 80

def evaluate_result(obtained, expected):
    global total_run_tests
    global num_success

    total_run_tests += 1
    if obtained == expected:
        num_success += 1
        ret = 'success'
    else:
        ret = 'fail'
    return ret
    
def calculate_summary():
    global total_run_tests
    global num_success

    return "Result:\nTotal run tests: {}, Total success: {} ({:0.2f} %)" \
        .format(total_run_tests, num_success, num_success / total_run_tests * 100)

def init_test():
    global total_run_tests
    global num_success

    total_run_tests = 0
    num_success = 0

def show_division():
    return '-' * DIVIDER_LEN

def new_test():
    print(show_division())

def finish_test():
    print(show_division())
    print(calculate_summary())
    print(show_division())
