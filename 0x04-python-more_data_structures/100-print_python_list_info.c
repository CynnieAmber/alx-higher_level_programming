#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list_info(PyObject *p);
/**
 * print_python_list_info - ===========
 * @p: ============
 * Description: =====
 * Return: ===========
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;
	 Py_ssize_t allocated = list->allocated;
	const char *str;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		str = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, str);
	}
}
