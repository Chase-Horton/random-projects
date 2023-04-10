<script>
    let wheel;
    export let rotate;
    export let data;
    export let labels;

    function delay(time) {
        return new Promise(resolve => setTimeout(resolve, time));
    }
    let prevIndex = 1

    let start = true;
    let index = 1
    let i;
    $:{ if(wheel && start) {
        let rows = wheel.children
        i = 1
        rows[i].children[1].style.background = "orange";
        prevIndex = i
        start = false
    }
    if (rotate != null) {
        if (rotate == -1) {
            index += 1
            if (index > data.length) {
                index = 1
            }
            wheel.children[index].children[1].style.background = "orange";
            wheel.children[prevIndex].children[1].style.background = "white";
            prevIndex = index
            rotate = null
        } else if (rotate >= 0) {
            index = rotate + 1
            wheel.children[index].children[1].style.background = "orange";
            wheel.children[prevIndex].children[1].style.background = "white";
            prevIndex = index
            rotate = null
        }
    }
}
</script>
<div>
    <div class="spinner-table"> 
        <table bind:this={wheel} class="dial">
            <tr><th colspan="2" style="padding: 5px 8px;  border: 2px solid black; background-color:#00CFC1;">MEM STRIP</th></tr>
			{#each data as d, i}
				<tr class="slice"><th>{labels[i]}:</th><td class="label">{d}</td></tr>
			{/each}
        </table>
    </div>
</div>
<style>
    table{
        border-collapse: collapse;
    }
    th{
        border: 1px solid black;
        padding:0px 0px;
        margin: 0px;
    }
    td{
        border: 1px solid black;
    }
</style>