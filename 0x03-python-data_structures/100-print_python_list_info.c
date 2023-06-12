#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - print python info using Cpython
 * @p: the python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	const char *type_ob;
	PyObject *item;
	PyTypeObject *ob;
	long int i;

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li \n", list->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		ob = item->ob_type;
		type_ob = ob->tp_name;
		printf("Element %li: %s\n", i, type_ob);
	}
}
