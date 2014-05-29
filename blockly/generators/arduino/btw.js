/**
 * @fileoverview Behind The Wire Landing Gear Servo Blocks
 * @author danse@jarofdoom.co.uk Richard Fontaine
 */
'use strict';

//define blocks
if (!Blockly.Language) Blockly.Language = {};

/////////////////////////////
//      Landing Gear       //
/////////////////////////////

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

//Define Landing Gear UP code
Blockly.Arduino.landing_gear_up = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_lg'] = 'functions.landingGearPrepare();\n';
	var code = 'functions.landingGearUp();\n';
	return code;
}

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

//Define Landing Gear down code
Blockly.Arduino.landing_gear_down = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_lg'] = 'functions.landingGearPrepare();\n';
	var code = 'functions.landingGearDown();\n';
	return code;
}

/////////////////////////////
//         Rudder          //
/////////////////////////////
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

//Define Rudder Left code
Blockly.Arduino.rudder_left = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_r'] = 'functions.rudderPrepare();\n';
	var code = 'functions.rudderLeft();\n';
	return code;
}

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

//Define Rudder Right code
Blockly.Arduino.rudder_right = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo_r'] = 'functions.rudderPrepare();\n';
	var code = 'functions.rudderRight();\n';
	return code;
}

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

/////////////////////////////
//          LEDs           //
/////////////////////////////
Blockly.Language.navigation_lights = {
	category: 'Navigation Lights',
	helpUrl: '',
	init: function() {
		this.setColour(230);
		this.appendDummyInput("")
			.appendTitle("Set  ")
			.appendTitle(new Blockly.FieldDropdown(profile.arduino_btw.nav_lights), "LED")
			.appendTitle("Light ")
			.appendTitle(new Blockly.FieldDropdown([["ON", "ON"], ["OFF", "OFF"]]), "STATE");
		this.setPreviousStatement(true);
		this.setNextStatement(true);
  }
};

Blockly.Arduino.navigation_lights = function() {
  var dropdown_pin = this.getTitleValue('LED');
  var dropdown_stat = this.getTitleValue('STATE');
  Blockly.Arduino.setups_['setup_output_'+dropdown_pin] = 'pinMode('+dropdown_pin+', OUTPUT);';
  var code = 'digitalWrite('+dropdown_pin+','+dropdown_stat+');\n'
  return code;
}

/////////////////////////////
//         Buttons         //
/////////////////////////////
Blockly.Language.read_button = {
	category: 'Read Button',
	helpUrl: '',
	init: function() {
		this.setColour(230);
		this.appendDummyInput("")
			.appendTitle("Check ")
			.appendTitle(new Blockly.FieldDropdown(profile.arduino_btw.buttons), "Button")
			.appendTitle(" Button");
		this.setOutput(true, Boolean);
		this.setTooltip('');
	}
};

Blockly.Arduino.read_button = function() {
  var dropdown_pin = this.getTitleValue('Button');
  Blockly.Arduino.setups_['setup_input_'+dropdown_pin] = 'pinMode('+dropdown_pin+', INPUT);';
  var code = 'digitalRead('+dropdown_pin+')';
  return [code, Blockly.Arduino.ORDER_ATOMIC];
};