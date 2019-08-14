#include "stdafx.h"

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <opencv2/core/mat.hpp>


using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
	Mat image;
	image = imread("circle1.jpg", IMREAD_COLOR); // Read the file
	Size size(6, 7);
	Mat outputarray;


	findCirclesGrid(image, size, outputarray);
	drawChessboardCorners(image, size, outputarray, 1);
	namedWindow("Display window", WINDOW_AUTOSIZE); // Create a window for display.
	imshow("Display window", image); // Show our image inside it.

	waitKey(0); // Wait for a keystroke in the window
	return 0;
}
