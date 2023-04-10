<script>
    export let wheel;
    export let test;
    export let color;
    export let reset;
	export let rotate;
	export let active;
	let angle = 0;
    function resetProgram(){
        reset();
		angle = 0;
		wheel.style.transform = "rotate(-" + angle + "deg)";
    }
    function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
    }
    $: {
        if(color != null){
            wheel.children[color[0]].style = "color:#07f246"
            delay(200).then(() => {
                wheel.children[color[0]].style = "color:white"
                color = null
            })
        }
    }
	$: if(rotate){
        angle += 360/11
        console.log('I SHOULD ROTATE')
        wheel.style.transform = "rotate(-" + angle + "deg)";
        rotate = false
    }
	$: if(active != null){
		console.log(active + " is active")
		wheel.children[active].style = "color:#07f246"
		delay(200).then(() => {
			wheel.children[active].style = "color:white"
			active = null
		})
	}
</script>
<div class="board">
    <div class="spinner-table"> 
        <div bind:this={wheel} class="dial">
            <div class="slice"><div class="label">increment()</div></div>
            <div class="slice"><div class="label">rotateMem()</div></div>
            <div class="slice"><div class="label">decrement()</div></div>
            <div class="slice"><div class="label">push()</div></div>
            <div class="slice"><div class="label">pop()</div></div>
            <div class="slice"><div class="label">outputStack()</div></div>
            <div class="slice"><div class="label">clr()</div></div>
            <div class="slice"><div class="label">compAB()</div></div>
            <div class="slice"><div class="label">sumAB()</div></div>
            <div class="slice"><div class="label">startWhile()</div></div>
            <div class="slice"><div class="label">endWhile()</div></div>
        </div>
    </div>
    <div class="arrow">
        <span class="pointer"></span>
    </div>
</div>


<button on:click={()=>test()}>Test</button>
<button style="margin-top: 70px;" on:click={() =>resetProgram()}>Reset</button>
<style lang="scss">
$diameter: 350px;
$numberOfSlices: 11;
$radius: calc($diameter / 2);
$circumfrance: calc(6.283185307 * $radius);
$sliceHeight: calc($circumfrance / $numberOfSlices);
$sliceOffeset: calc($sliceHeight / 2);
$sliceColor: #095B8D;
$rotation: calc(360deg / $numberOfSlices);
$timeout: 500ms;

.spinner-table {
	height: ($diameter - 2px);
	width: ($diameter - 2px);
	position: relative;
	border-radius: 100%;
	overflow: hidden;
}

.dial {
	height: 100%;
	transition: all $timeout ease-out;
	animation-fill-mode: forwards;
	animation-timing-function: linear;
	
	
	&:before {
		content: '';
		text-align: center;
		display: block;
		line-height: 60px;
		position: absolute;
		height: 40px;
		width: 40px;
		background: white;
		box-shadow: 0 0 5px 5px rgba(#000, .1);
		top: 50%;
		left: 50%;
		margin-top: -20px;
		margin-left: -20px;
		border-radius: 100%;
		z-index: 200;
	}

	.slice {
		z-index: 150;
		position: absolute;
		top: calc(50% - #{$sliceOffeset});
		height: $sliceHeight;
		left: 50%;
		width: 50%;
		color: white;
		text-align: right;
		padding-right: 10px;
		display: block;
		transform-origin: left center;
		
		&:before,
		&:after {
			content: "";
			display: block;
			width: 0;
			height: 0;
			border-style: solid;
		}

		&:before {
			margin-bottom: -1px;
			margin-top: -2px;
			border-width: 0 0 (calc($sliceHeight / 2) + 4px) $radius;
			border-color: transparent transparent $sliceColor transparent;
		}

		&:after {
			margin-top: -1px;
			margin-bottom: -2px;
			border-width: 0 $radius (calc($sliceHeight / 2) + 4px) 0;
			border-color: transparent $sliceColor transparent transparent;
		}
		
		&:nth-child(even) {
	
			&:after { border-color: transparent darken($sliceColor, 10%) transparent transparent; }
			&:before { border-color: transparent transparent darken($sliceColor, 10%) transparent; }
		}

		.label {
			position: absolute;
			top: 0;
			bottom: 0;
			width: 70%;
			line-height: $sliceHeight;
			padding-top: 1px;
			padding-bottom: 1px;
			font-size: 16px;
			text-align: right;
			padding-left: 20px;
		}

		&:nth-child(1) {
			transform: rotate(0deg);
		}
		&:nth-child(2) {
			transform: rotate(32.7deg);
		}
		&:nth-child(3) {
			transform: rotate(65.45deg);
		}
		&:nth-child(4) {
			transform: rotate(98.18deg);
		}
		&:nth-child(5) {
			transform: rotate(130.90deg);
		}
		&:nth-child(6) {
			transform: rotate(163.63deg);
		}
		&:nth-child(7) {
			transform: rotate(196.36deg);
		}
		&:nth-child(8) {
			transform: rotate(229.09deg);
		}
		&:nth-child(9) {
			transform: rotate(261.81deg);
		}
		&:nth-child(10) {
			transform: rotate(294.54deg);
		}
		&:nth-child(11) {
			transform: rotate(327.27deg);
		}
	}
}

.arrow {
	position: absolute;
	height: 30px;
	width: 50px;
	left: ($diameter + 30px);
	z-index: 500;
	display: block;
	top: 50%;
	margin-top: -15px;
	transform-origin: center right;
}

.pointer {
	z-index: 500;
	display: block;
	height: 30px;
	width: 50px;
	
	&:before {
		content: '';
		display: block;
		position: absolute;
		right: 0;
		top: 0;
		width: 0;
		height: 0;
		border-style: solid;
		border-width: 0 0 15px 50px;
		border-color: transparent transparent #c27028 transparent;
	}
	&:after {
		content: '';
		display: block;
		position: absolute;
		right: 0;
		bottom: 0;
		width: 0;
		height: 0;
		border-style: solid;
		border-width: 0 50px 15px 0;
		border-color: transparent #c27028 transparent transparent;
	}
}

.board {
	position: relative;
	background: white;
	padding: 50px;
}

button {
	background: #c27028;
	border: 0;
	padding: 15px 50px;
	color: white;
	position: absolute;
	top: 50%;
	margin-top: -20px;
	right: 20%;
}
</style>