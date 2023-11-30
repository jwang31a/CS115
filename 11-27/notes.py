#selection and quick sort

sample = {"asdf" : 1, "bsdf" : 3}
artist1 = "asdf\n"
sample[artist1[:-1]] += 1
print(sample)

usernames = ["name1", "name1\n", "name3", "not a name"]

for n in usernames:
    sample[n] += 1