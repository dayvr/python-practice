# Test utils

class TestTools():
    DIVIDER_LENGTH = 60

    def __init__(self):
        self.total_run_tests = 0
        self.num_success = 0
        self.test_msg = ''
        self.test_result = ''
        self.show_obtained = False
    
    def __del__(self):
        print('\n' + self.show_result_division())
        print(self.calculate_summary())
        print(self.show_result_division() + '\n')

    def new_test(self, msg='', show=True, func=''):
        self.test_msg = msg
        self.show_obtained = show
        if func:
            self.test_msg += func.__name__
        print(self.show_test_division())

    def evaluate_result(self, obtained, expected):
        self.total_run_tests += 1

        if obtained == expected:
            self.num_success += 1
            self.test_result = 'success'
        else:
            self.test_result = 'fail'
        
        if self.test_msg:
            self.show_result()

        if self.show_obtained:
            print("Output: {}".format(obtained))
            
        return self.test_result

    def calculate_summary(self):
        try:
            printing_summary = "Summary\nTotal run tests: {}, Total success: {} ({:0.2f} %)" \
                                .format(self.total_run_tests, self.num_success, 
                                self.num_success / self.total_run_tests * 100)
        except ZeroDivisionError:
            printing_summary = 'Try it again!'
        return printing_summary

    def show_test_division(self):
        return ''

    def show_result_division(self):
        return '-' * self.DIVIDER_LENGTH

    def show_result(self):
        print("Test {}: {} -> {}"
            .format(self.total_run_tests, self.test_msg, self.test_result))


if __name__ == '__main__':
    # Unitary Tests
    # Test exception in destructor
    t = TestTools()
    del(t)# 