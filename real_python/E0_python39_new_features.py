"""
simpler updating of dicts
"""

# several ways to merge two dicts

zoo_rome = {"wolves": 4, "tigers": 3, "elephants": 5}
zoo_wro = {"monkeys": 10, "wolves": 5, "cobras": 10}

# 1st way to merge
zoos = {**zoo_rome, **zoo_wro}
print(zoos) # wolves from rome are overwritten by wolves from wro !

# 2nd
merged = zoo_rome.copy()
for k, v in zoo_wro.items():
    merged[k] = v
print(merged)  # also overwrites wolves

# 3rd update dict in place:
zoo_rome_wro = zoo_rome.copy()
zoo_rome_wro.update(zoo_wro)
print(zoo_rome_wro)
zoo_rome_wro = zoo_rome_wro.copy().update(zoo_wro) # does not work update does not return
print(zoo_rome_wro)
print(zoo_rome, zoo_wro)

# 4th
(zoo_rome_wro := zoo_rome.copy()).update(zoo_wro)
print(zoo_rome_wro)

# python3.9 - new operators for dicts:
# union (|)
# in place union (|=)

a = zoo_rome | zoo_wro 
