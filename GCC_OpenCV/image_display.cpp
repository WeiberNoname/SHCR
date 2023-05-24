#include <Python.h>
#include <opencv2/opencv.hpp>

#ifdef __cplusplus
extern "C" {
#endif

static PyObject* display_image(PyObject* self, PyObject* args) {
    const char* image_path;
    if (!PyArg_ParseTuple(args, "s", &image_path)) {
        return NULL;
    }

    cv::Mat image = cv::imread(image_path);
    if (image.empty()) {
        PyErr_SetString(PyExc_RuntimeError, "Failed to open image");
        return NULL;
    }

    cv::namedWindow("Image", cv::WINDOW_NORMAL);
    cv::imshow("Image", image);
    cv::waitKey(0);

    Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
    {"display_image", display_image, METH_VARARGS, "Display an image"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "image_display",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_image_display(void) {
    return PyModule_Create(&module);
}

#ifdef __cplusplus
}
#endif
