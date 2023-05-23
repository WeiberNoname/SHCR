#include <Python.h>

// Function definition
static PyObject* my_library_greet(PyObject* self, PyObject* args) {
    const char* name;

    // Parse the arguments
    if (!PyArg_ParseTuple(args, "s", &name)) {
        return NULL;
    }

    // Generate the greeting message
    char message[100];
    snprintf(message, sizeof(message), "Hello, %s!", name);

    // Create a Python string from the message
    PyObject* result = Py_BuildValue("s", message);

    return result;
}

// Method table
static PyMethodDef my_library_methods[] = {
    {"greet", my_library_greet, METH_VARARGS, "Greet the user."},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Module definition
static struct PyModuleDef my_library_module = {
    PyModuleDef_HEAD_INIT,
    "my_library",
    "A simple C library for Python",
    -1,
    my_library_methods
};

// Module initialization function
PyMODINIT_FUNC PyInit_my_library(void) {
    return PyModule_Create(&my_library_module);
}
