def can_drive(age):
	driving_age = 16
	return age >= driving_age

def test_16():
	assert can_drive(16)

def test_15():
	assert not can_drive(15)

