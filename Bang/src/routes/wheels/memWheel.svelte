<script>
    let wheel;
	let angle = 0;
    export let rotate;
    export let data;
	export let reset
    $: if(rotate){
        angle += 120
        //console.log('I SHOULD ROTATE')
        wheel.style.transform = "rotate(-" + angle + "deg)";
        rotate = false
    }
	$: if(wheel){
		let a = 360/3
		for(let i = 0; i < 3; i++) {
			wheel.children[i].style.transform = "rotate(" + a * i + "deg)";
		}
	}
	$: if(reset){
		angle = 0
		wheel.style.transform = "rotate(-" + angle + "deg)";
		reset = false
	}
</script>
<div class="board">
    <div class="spinner-table"> 
        <div bind:this={wheel} class="dial">
            <div class="slice"><div class="label"><strong>A: </strong>{data[0]}</div></div>
            <div class="slice"><div class="label"><strong>B: </strong>{data[1]}</div></div>
            <div class="slice"><div class="label"><strong>X: </strong>{data[2]}</div></div>
        </div>
    </div>
    <div class="arrow">
        <span class="pointer"></span>
    </div>
</div>


<style lang="scss">
$diameter: 350px;
$numberOfSlices: 1;
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
			transition: all 0.5s ease;
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
		display:inline-block;
	padding: 50px;
}
</style>