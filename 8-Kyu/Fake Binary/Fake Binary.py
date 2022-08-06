def fake_bin(x):
	ans = ""
	for char in x:
		if char < '5':
			ans += '0'
		else:
			ans += '1'
	return ans