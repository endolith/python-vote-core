def unique_permutations(xs):
	if len(xs) < 2:
		yield xs
	else:
		h = []
		for x in xs:
			h.append(x)
			if x in h[:-1]:
				continue
			ts = xs[:]
			ts.remove(x)
			for ps in unique_permutations(ts):
				yield [x]+ps
