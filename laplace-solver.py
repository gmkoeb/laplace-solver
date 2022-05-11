from dolfin import *
import matplotlib.pyplot as plt
# Create mesh and define function space
# Define boundary condition
mesh = Mesh("Te3.xml")
subdomains = MeshFunction("size_t", mesh, "Te3_physical_region.xml")
boundaries = MeshFunction("size_t", mesh, "Te3_facet_region.xml")
V=FunctionSpace(mesh,'CG',2)

Etopleft = DirichletBC(V, -1, boundaries,2)
Etopright=DirichletBC(V, 1, boundaries, 3)
Ebottomleft=DirichletBC(V, 1, boundaries, 4)
Ebottomright=DirichletBC(V, -1, boundaries, 5)

bc = [Etopleft,Etopright,Ebottomleft,Ebottomright]

u_D=Constant(0.0)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(0.0)
a = dot(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc)
# Save solution to file in VTK format
vtkfile = File('poisson/potential.pvd')
vtkfile << u

# Compute error in L2 norm
error_L2 = errornorm(u_D, u, 'L2')

# Compute maximum error at vertices
vertex_values_u_D = u_D.compute_vertex_values(mesh)
vertex_values_u = u.compute_vertex_values(mesh)
import numpy as np
error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))
# Print errors
print('error_L2  =', error_L2)
print('error_max =', error_max)
# Hold plot
E=project(-grad(u))
efieldfile = File('poisson/efield.pvd')
efieldfile << E

plt.figure(figsize=(12,7))
pp = plot(u, zorder=3)
plt.colorbar(pp)
plt.title("Electric Potential")
plt.show()

