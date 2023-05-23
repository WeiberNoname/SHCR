#include <Python.h>

// Function definition
static PyObject* library_greet(PyObject* self, PyObject* args) {
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
static PyMethodDef library_methods[] = {
    {"greet", library_greet, METH_VARARGS, "Greet the user."},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Module definition
static struct PyModuleDef library_module = {
    PyModuleDef_HEAD_INIT,
    "library",
    "A simple C library for Python",
    -1,
    library_methods
};

// Module initialization function
PyMODINIT_FUNC PyInit_library(void) {
    return PyModule_Create(&library_module);
}
