<script>
	export let sliceNames = [];
    let wheel;
    export let test;
	export let rotate;
    export let SLEEPTIME;
    export let active;

    function delay(time) {
        return new Promise(resolve => setTimeout(resolve, time));
    }
    let prevIndex = 1

    let start = true;
    let index = 1
    $:{ if(wheel && start) {
        wheel.children[index].style.background = "orange";
        start = false
    }
    if (rotate != null) {
        if (rotate == -1) {
            index += 1
            if (index > sliceNames.length) {
                index = 1
            }
            wheel.children[index].style.background = "orange";
            wheel.children[prevIndex].style.background = "white";
            prevIndex = index
            rotate = null
        } else if (rotate >= 0) {
            console.log("SNIPING")
            index = rotate + 1
            wheel.children[index].style.background = "orange";
            wheel.children[prevIndex].style.background = "white";
            prevIndex = index
            rotate = null
        }
    }
    if(active != null){
        let i = index
        wheel.children[index].style.background = "#49fb35";
        delay(SLEEPTIME/2).then(() => {
            wheel.children[index].style.background = "orange";
        active = null
		})
    }
}
</script>
<div style="margin-right:10px">
    <div class="spinner-table"> 
        <table bind:this={wheel} class="dial">
            <th>OP STRIP</th>
			{#each sliceNames as sliceName}
				<tr class="slice"><td class="label">{sliceName}</td></tr>
			{/each}
        </table>
    </div>
	
</div>
<style>
    table{
        border-collapse: collapse;
    }
    th{
        border: 2px solid black;
        padding: 5px, 8px;
        background-color: #00CFC1;
    }
    td{
        border: 1px solid black;
    }
</style>