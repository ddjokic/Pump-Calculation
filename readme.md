<h4>Pump Calculations</h4>

Few calculations which can be easily performed by hand:</p>

<h5>1. Shaft Power</h5>

Big issue here is Pump efficiency, which is defined as ratio of power we get out of the pump to the amount of power we are putting into the pump. Survey among popular pump brand shows that efficiency of the pump is in range of 40-90%. Seems that efficiency is related to "speed number" and dropping if speed number is below 1000. Wear of sealing elements inside pump housing affect efficiency.</p>
Default efficiency, used in script, is **0.6**.</p>
Vapour pressure data for few fluids can be found [here](https://github.com/ddjokic\Headloss in Pipe\Fluids.md).

<h5>2. NPSHa and Cavitation</h5>

For cavitation not to occur, minimum pressure on suction side should be grater that vapour pressure of the liquid at operation temperature. Script calculates minimum pressure and compare it with vapour pressure (user defined).</p>

<h5>3. Centrifugal Pump Curve</h5>

Useful if one needs Pump Curve H-Q equation, based on given points - eg. maker's graph. As characteristic of centrifugal pump is parabola, at least three points should be prvided. More points - better fitt.
