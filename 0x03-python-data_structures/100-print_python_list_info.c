#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: PyObject
 * 
 *Return: void 
 */

void print_python_list_info(PyObject *p)
{
    Py_ssize_t i;
    Py_ssize_t size;
    PyObject *item;

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %ld\n", i, PyLong_AsLong(item));
    }
}
