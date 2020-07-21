#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/6/17 下午1:36
# @Author  : Hanley
# @File    : scheme.py
# @Desc    : 

class Scheme(object):
    # mysql schemes
    PEEWEE_SCHEMES = {
        'apsw',
        'mysql',
        'mysql+pool',
        'postgres',
        'postgres+pool',
        'postgresext',
        'postgresql+pool',
        'sqlite',
        'sqliteext'
        'sqlite+pool',
        'sqliteext+pool',
    }

    # mongodb uri schemes
    MONGODB_SCHEMES = {
        'mongodb'
    }

    HELLO = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string", "examples": ["YQ"]
            }
        },
        "required": [
            "name"
        ]
    }

    TEST_SCHEMES = {
        "type": "array",
        "title": "create order Scheme",
        "items": {
            "type": "object",
            "required": [
                "commodity_list"
            ],
            "properties": {
                "commodity_amount": {
                    "type": "number", "examples": [199.393]
                },
                "commodity_list": {
                    "type": "array",
                    "title": "commodity info list",
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "number"
                        ],
                        "properties": {
                            "id": {
                                "type": "string",
                                "examples": ["943f9326ijs311ea99"]
                            },
                            "name": {
                                "type": "string",
                                "examples": ["华夫饼"]
                            },
                            "price": {
                                "type": "number",
                                "examples": [199.393]
                            },
                            "number": {
                                "type": "integer",
                                "examples": [3]
                            }
                        }
                    }
                }
            }
        }
    }
