#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len;
	PyVarObject* size;
	PyVarObject* type;
	PyObject *temp;
	Py_ssize_t i;

	len = PyList_Size(p);
	size = Py_SIZE(p);
	printf("[*] Size of Python List = %zd\n", len);
	printf("[*] Allocated = %zd\n", size);
	for (i = 0; i < len; i++)
	{
		temp = PyList_GetItem(p, i);
		type = Py_SIZE(temp);
		printf("Element %zd: ??\n", type);
	}
}
