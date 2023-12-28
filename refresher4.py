
if __name__ == '__main__':
    def fn_restricted_params(only_positional, /, positional_or_kw, *, kw):
        print("positional:", only_positional)
        print("positional or kw:", positional_or_kw)
        print("kw:", kw)


    fn_restricted_params(34, "foo", kw="Keyword arg")


    def exponen(base):
        """
        Returns a lambda function that returns specified power of base
        :param base: the base
        :return: base ** power
        """
        # returns a function defined as a lambda expression
        return lambda power: base ** power  # power is the parameter/argument passed to the lambda function


    power_up = exponen(3)
    print(power_up(4))
    print(power_up(8))
    print(power_up(5))

