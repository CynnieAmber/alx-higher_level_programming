#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - ===========
 * @p: ============
 * Description: =====
 * Return: ===========
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytesObj;
	Py_ssize_t size, i;
	char *strcontent;
	char *bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytesObj = (PyBytesObject *)p;
	size = bytesObj->ob_base.ob_size;
	strcontent = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", strcontent);
	if (size > 0)
	{
		if (size > 10)
		{
			printf("  first 10 bytes:");
			size = 9;
		}
		else if (size > 0 && size <= 10)
		{
			printf("  first %ld bytes:", size + 1);
		}
		bytes = PyBytes_AsString(p);
		for (i = 0; i < size + 1; i++)
		{
			printf(" %02x", (unsigned char)bytes[i]);
		}
	}
	printf("\n");
}
/**
 * print_python_list - ===========
 * @p: ============
 * Description: =====
 * Return: ===========
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
