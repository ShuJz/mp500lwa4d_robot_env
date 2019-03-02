// Auto-generated. Do not edit!

// (in-package robot_service.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class RLChooseActionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RLChooseActionRequest
    // Serialize message field [state]
    bufferOffset = _arraySerializer.float64(obj.state, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RLChooseActionRequest
    let len;
    let data = new RLChooseActionRequest(null);
    // Deserialize message field [state]
    data.state = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.state.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_service/RLChooseActionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c30e6364d50c603d25671fea66595c53';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] state
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RLChooseActionRequest(null);
    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = []
    }

    return resolved;
    }
};

class RLChooseActionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.action = null;
    }
    else {
      if (initObj.hasOwnProperty('action')) {
        this.action = initObj.action
      }
      else {
        this.action = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RLChooseActionResponse
    // Serialize message field [action]
    bufferOffset = _arraySerializer.float64(obj.action, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RLChooseActionResponse
    let len;
    let data = new RLChooseActionResponse(null);
    // Deserialize message field [action]
    data.action = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.action.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot_service/RLChooseActionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '79f44d272f2ebe04451185b0dea57684';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] action
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RLChooseActionResponse(null);
    if (msg.action !== undefined) {
      resolved.action = msg.action;
    }
    else {
      resolved.action = []
    }

    return resolved;
    }
};

module.exports = {
  Request: RLChooseActionRequest,
  Response: RLChooseActionResponse,
  md5sum() { return '6904b829fd6bdbea4739bf92ec4b118d'; },
  datatype() { return 'robot_service/RLChooseAction'; }
};
