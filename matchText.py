def match(a, b) :
	return SequenceMatcher(None, a, b).ratio()