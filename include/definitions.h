#ifndef DEFINITIONS_H
#define DEFINITIONS_H

#include <chrono>
#include <string>
#include <vector>
#include <thread>
#include <cstdlib>
#include <fstream>
#include <iostream>

//C Includes
#include <stdio.h>
#include <stdlib.h>


using namespace std;

enum Algorithm {
    ROUND_ROBIN,
    LOTTERY,
    PRIORITY
};

static pthread_rwlock_t rw_lock = PTHREAD_RWLOCK_INITIALIZER;
static pthread_mutex_t  mutex = PTHREAD_MUTEX_INITIALIZER;
static bool PAUSED = false;
static int DELAY = 50;

#endif