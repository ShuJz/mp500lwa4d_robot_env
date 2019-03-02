// Auto-generated. Do not edit!

// (in-package robot_service.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class RLMemoryStore {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.s = null;
      this.a = null;
      this.r = null;
      this.s_ = null;
    }
    else {
      if (initObj.hasOwnProperty('s')) {
        this.s = initObj.s
      }
      else {
        this.s = [];
      }
      if (initObj.hasOwnProperty('a')) {
        this.a = initObj.a
      }
      else {
        this.a = [];
      }
      if (initObj.hasOwnProperty('r')) {
        this.r = initObj.r
      }
      else {
        this.r = 0.0;
      }
      if (initObj.hasOwnProperty('s_')) {
        this.s_ = initObj.s_
      }
      else {
        this.s_ = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RLMemoryStore
    // Serialize message field [s]
    bufferOffset = _arraySerializer.float64(obj.s, buffer, bufferOffset, null);
    // Serialize message field [a]
    bufferOffset = _arraySerializer.float64(obj.a, buffer, bufferOffset, null);
    // Serialize message field [r]
    bufferOffset = _serializer.float64(obj.r, buffer, bufferOffset);
    // Serialize message field [s_]
    bufferOffset = _arraySerializer.float64(obj.s_, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RLMemoryStore
    let len;
    let data = new RLMemoryStore(null);
    // Deserialize message field [s]
    data.s = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [a]
    data.a = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [r]
    data.r = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [s_]
    data.s_ = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.s.length;
    length += 8 * object.a.length;
    length += 8 * object.s_.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_service/RLMemoryStore';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ee95e3c395c129a7450df7cde8e1479b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] s
    float64[] a
    float64 r
    float64[] s_
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RLMemoryStore(null);
    if (msg.s !== undefined) {
      resolved.s = msg.s;
    }
    else {
      resolved.s = []
    }

    if (msg.a !== undefined) {
      resolved.a = msg.a;
    }
    else {
      resolved.a = []
    }

    if (msg.r !== undefined) {
      resolved.r = msg.r;
    }
    else {
      resolved.r = 0.0
    }

    if (msg.s_ !== undefined) {
      resolved.s_ = msg.s_;
    }
    else {
      resolved.s_ = []
    }

    return resolved;
    }
};

module.exports = RLMemoryStore;
