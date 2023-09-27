import math

# 調べたい範囲の下限値、上限値を定義
from_num = 1
to_num = 10000


def prime_num(from_num, to_num):
	"""

	from_num ~ to_numまでの素数を求める関数

	Args:
		from_num(int or float): 求めたい友愛数の範囲の最小値
		to_num(int or float): 求めたい友愛数の範囲の最大値

	Returns:
		from_num ~ to_numの範囲内の素数のリスト(戻り値)

	"""
	# 0 ~ 上限値までを全て素数であると設定してリスト化する
	num_li = [True] * to_num

	# 0と1は素数ではないため予め素数から除外する
	num_li[0], num_li[1] = False, False

	# (2 ~ 上限値の平方根)で割り切れる数値を除外する
	for i in range(2, (int(math.sqrt(to_num))) + 1):
		if num_li[i]:
			for j in range(i ** 2, to_num, i):
				num_li[j] = False


	# 除外されなかった数(素数)のみを抽出しリスト化する
	prime_num_li = [i for i, num in enumerate(num_li) if num]

	# 下限値 ~ 上限値の偶数以外を全て素数であると設定してリスト化する
	numbers = [False if (k + from_num) % 2 == 0 and k + from_num != 2 else True for k in range(to_num - from_num + 1)]

	# 下限値 ~ 上限値の中で合成数を除外する
	for m, number in enumerate(numbers):
		if (m + from_num) % 2 == 0:
			continue
		for p in prime_num_li:
			if (m + from_num) % p == 0 and (m + from_num) != p:
				numbers[m] = False
				break

	# 除外されなかった数(素数)のリストを戻り値として返す
	return [n + from_num for n, number in enumerate(numbers) if number]


def composite_num(from_num, to_num):
	"""

	from_num ~ to_numまでの合成数を求める関数

	Args:
		from_num(int or float): 求めたい友愛数の範囲の最小値
		to_num(int or float): 求めたい友愛数の範囲の最大値

	Returns:
		from_num ~ to_numの範囲内の合成数のリスト(戻り値)

	"""
	# prime_num関数の戻り値を取得
	primes = prime_num(from_num, to_num)

	# 下限値 ~ 上限値の数をリスト化
	num_li = [i for i in range(from_num, to_num + 1)]

	# 合成数のリストを戻り値として返す
	return list(set(num_li) - set(primes))


def amicable_num(from_num, to_num):
	"""

	友愛数を求める関数

	Args:
		from_num(int or float): 求めたい友愛数の範囲の最小値
		to_num(int or float): 求めたい友愛数の範囲の最大値

	Returns:
		from_num ~ to_numの範囲内の友愛数の組を2重リストで出力

	"""
	# 合成数のリストを取得
	composite_num_li = composite_num(from_num, to_num)

	# 各数の真の約数のリストを初期化
	divisor_li = []

	# 各数の真の約数の和のリストを初期化
	sum_divisor_li = []

	# 各数の真の約数の和をリストへ追加
	for n in composite_num_li:
		divisors = [1]
		for i in range(2, int(math.sqrt(n)) + 1, 1):
			if n % i == 0:
				quotient = n // i
				divisors.append(quotient)
				if quotient != i:
					divisors.append(i)
		sum_divisor = sum(divisors)
		sum_divisor_li.append(sum_divisor)

	# 友愛数のペアの2重リストを初期化
	amicable_nums = []

	# 合成数のリストをセット型にする
	composite_num_li_set = set(composite_num_li)

	# 合成数と対応する真の約数の辞書を作成
	div_and_com_dict = {composite_num_li[j]: sum_divisor_li[j] for j in range(len(composite_num_li))}

	# 友愛数のペアを2重リストで取得
	for j, divisor in enumerate(sum_divisor_li):
		if divisor in composite_num_li_set and div_and_com_dict[divisor] == composite_num_li[j] and divisor != composite_num_li[j]:
			amicable_pair = []
			amicable_pair.append(composite_num_li[j])
			amicable_pair.append(divisor)
			amicable_pair.reverse()
			if amicable_pair not in amicable_nums:
				amicable_pair.reverse()
				amicable_nums.append(amicable_pair)

	# 友愛数のペアの2重リストを出力
	print(amicable_nums)


if __name__ == "__main__":
	amicable_num(from_num, to_num)