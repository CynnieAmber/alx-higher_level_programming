#include <stdio.h>
#include <Python.h>
/**
 * print_python_string - string object
 * @p: pyobject
 * Description: string object info
 * Return: 0
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (PyUnicode_CheckExact(p))
	{
		PyUnicode_READY(p);
		Py_UNICODE *value = PyUnicode_AS_UNICODE(p);
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);
		int is_ascii = PyUnicode_IS_ASCII(p);


		printf("  type: %s\n",
				is_ascii ? "compact ascii" : "compact unicode object");
		printf("  length: %zd\n", length);
		printf("  value: %ls\n", value);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
