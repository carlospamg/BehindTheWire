/**
 * @fileoverview Behind The Wire Landing Gear Servo Blocks
 * @author danse@jarofdoom.co.uk Richard Fontaine
 */
'use strict';

//define blocks
if (!Blockly.Language) Blockly.Language = {};

//Define Landing Gear UP block
Blockly.Language.landing_gear_up = {
	category:'Landing Gear',
	helpUrl:'',
	init: function(){
		this.setColour(0);
		this.appendDummyInput("")
			.appendTitle("Move landing gear up");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
	}
};

//Define Landing Gear down block
Blockly.Language.landing_gear_down = {
	category:'Landing Gear',
	helpUrl:'',
	init: function(){
		this.setColour(0);
		this.appendDummyInput("")
			.appendTitle("Move landing gear down");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
	}
};

//Define Rudder Left block
Blockly.Language.rudder_left = {
	category:'Rudder',
	helpUrl:'',
	init: function(){
		this.setColour(0);
		this.appendDummyInput("")
			.appendTitle("Move rudder Left");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
	}
};

//Define Rudder Right block
Blockly.Language.rudder_right = {
	category:'Rudder',
	helpUrl:'',
	init: function(){
		this.setColour(0);
		this.appendDummyInput("")
			.appendTitle("Move rudder Right");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
	}
};

//Define Rudder Set Position block
Blockly.Language.rudder_set_position = {
	category:'Rudder',
	helpUrl:'',
	init: function(){
		this.setColour(0);
		this.appendValueInput("RUDDER_POSITION", Number)
		    .appendTitle("Rudder position to ")
		    .setCheck(Number);
		this.setInputsInline(true);
		this.setPreviousStatement(true);
		this.setNextStatement(true);
		this.setTooltip('Set the rudder position to 0-180');
	}
};

//Define Landing Gear UP code
Blockly.Arduino.landing_gear_up = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_lg'] = 'functions.landingGearPrepare();\n';
	var code = 'functions.landingGearUp();\n';
	return code;
}

//Define Landing Gear down code
Blockly.Arduino.landing_gear_down = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_lg'] = 'functions.landingGearPrepare();\n';
	var code = 'functions.landingGearDown();\n';
	return code;
}

//Define Rudder Left code
Blockly.Arduino.rudder_left = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_r'] = 'functions.rudderPrepare();\n';
	var code = 'functions.rudderLeft();\n';
	return code;
}

//Define Rudder Right code
Blockly.Arduino.rudder_right = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_r'] = 'functions.rudderPrepare();\n';
	var code = 'functions.rudderRight();\n';
	return code;
}

//Define Rudder Set Position code
Blockly.Arduino.rudder_set_position = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_r'] = 'functions.rudderPrepare();\n';
	var servo_position =
		Blockly.Arduino.valueToCode(this, 'RUDDER_POSITION', Blockly.Arduino.ORDER_ATOMIC) ||
		'90';
	var code = 'functions.rudderSetPosition(' + servo_position + ');\n';
	return code;
}
