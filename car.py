# -*- coding:utf-8 -*-
"""
author: Zoupers
create: 2020/1/13 21:33
file name: car
description:
    给小车发送信号的接口
"""
import requests


class Car:
    @staticmethod
    def fast():
        """
        换高速档
        :return:
        """
        return True

    @staticmethod
    def slow():
        """
        换低速档
        :return:
        """
        return True

    @staticmethod
    def forward(x=0.5):
        """
        前进
        :param x:
        :return:
        """
        return True

    @staticmethod
    def backward(x=0.5):
        """
        后退
        :param x:
        :return:
        """
        return True

    @staticmethod
    def pre_lock():
        """
        锁前轮
        :return:
        """
        return True

    @staticmethod
    def pre_open():
        """
        开前轮
        :return:
        """
        return True

    @staticmethod
    def back_lock():
        """
        锁后轮
        :return:
        """
        return True

    @staticmethod
    def back_open():
        """
        开后轮
        :return:
        """
        return True


