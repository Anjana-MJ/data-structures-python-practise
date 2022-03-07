class TwoSum:
    def find_two_sum(self, data_list, target):
        prev_hash = {}
        for i, n in enumerate(data_list):
            diff = target - n
            if diff in prev_hash:
                return [prev_hash[diff], i]
            prev_hash[n] = i
        return


if __name__ == '__main__':
    tsum = TwoSum()
    result = tsum.find_two_sum([2, 3, 5, 1], 4)
    print(result)
