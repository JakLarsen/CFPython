sidesMap = {
			'Tetrahedron': 4,
			'Cube': 6, 
			'Octahedron': 8, 
			'Dodecahedron': 12,
			'Icosahedron': 20
			}

t = int(input())

summer = 0

for t in range(t):
	summer += sidesMap[input()]
print(summer)
