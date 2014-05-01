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

//Define Landing Gear UP code
Blockly.Arduino.landing_gear_up = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo'] = 'functions.landingGearPrepare();\n';
	var code = 'functions.landingGearUp();\n';
	return code;
}

//Define Landing Gear down code
Blockly.Arduino.landing_gear_down = function() {
	Blockly.Arduino.definitions_['define_servo'] = '#include <Servo.h>\n';
	Blockly.Arduino.setups_['prepare_servo'] = 'functions.landingGearPrepare();\n';
	var code = 'functions.landingGearDown();\n';
	return code;
}