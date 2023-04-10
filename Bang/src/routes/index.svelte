<script lang="ts">
    const DEVEL = true;
    const ROTATION = true;
    let SLEEPTIME = 1000;
    function sleep() {
        return new Promise(resolve => setTimeout(resolve, SLEEPTIME));
    }
    import Wheel from './wheels/wheelSmall.svelte'
    import MemWheel from './wheels/memWheel.svelte'
    
    function test(){
      D.acceptString('!?!!?!?!?!?!?!?????!!??!????!????!???????!?!')
    }
    type nullNum = number | null;
    type nullString = string | null;
    class discoids {
        opDial;
      program:string = '';
      numOfMemDials:number;
      memDial:number[];
      originMemDial:number[];
      stack:number[] = [];
      memIndex:number;
      opIndex:number;
      startMemIndex:number;
      startOpIndex:number;
      currentMemWatchCell:nullNum;
      rotateMemAmt:number;
      rotateOpAmt:number;
      a:number;
      b:number;
      progIndex:number;
      opDialNames:string[] = [];

      constructor(startMemIndex:number, startOpIndex:number, memDial:number[], rotateMemAmt:number, rotateOpAmt:number){
        this.opDial = [this.increment, this.rotateMem, this.inputStack, this.pop, this.startWhile, this.sumAB, this.outputStack, this.swap, this.decrement, this.endWhile];
        this.numOfMemDials = memDial.length;
        this.memDial = memDial;
        this.originMemDial = [...memDial];
        this.memIndex = startMemIndex;
        this.startMemIndex = startMemIndex;
        this.opIndex = startOpIndex;
        this.startOpIndex = startOpIndex;
        this.currentMemWatchCell = null;
        this.rotateMemAmt = 1;
        this.rotateOpAmt = 1;
        this.a = 0;
        this.b = 1;
        this.progIndex = 0;
        this.stack = [];

        for(let op of this.opDial){
          this.opDialNames.push(op.name + '()') 
        }
      }
        getOp(){
          return this.opDial[this.opIndex]
        }
        rotateOp(){
          this.opIndex += this.rotateOpAmt
          if(this.opIndex >= this.opDial.length) {
            this.opIndex = 0
          } else if(this.opIndex < 0) {
            this.opIndex = this.opDial.length -1
          }
          if(ROTATION) console.log('rotating op dial: ' + this.opDial[this.opIndex].name)
          setOpRoation = -1;
        }
        swap(){
          if(DEVEL) console.log('swapping')
          let temp = this.memDial[this.a]
          this.memDial[this.a] = this.memDial[this.b]
          this.memDial[this.b] = temp
          MEM_DATA_OUT = [...this.memDial]
        }
        //operations
        rotateMem(){
          if(DEVEL) console.log('rotating memory dial')
          this.memIndex += this.rotateMemAmt
          if(this.memIndex >= this.memDial.length) {
            this.memIndex = 0
          } else if(this.memIndex < 0) {
            this.memIndex = this.memDial.length -1
          }
          setRotation = true;
        }
        increment(){
          if(DEVEL) console.log('incrementing')
          this.memDial[this.memIndex] += 1
          MEM_DATA_OUT = [...this.memDial]
        }
        decrement(){
          if(DEVEL) console.log('decrementing')
          this.memDial[this.memIndex] -= 1
          MEM_DATA_OUT = [...this.memDial]
        }
        push(){
          if(DEVEL) console.log('pushing to stack')
          this.stack.push(this.getMem())
          stack = [...this.stack]
        }
        pop(){
          if(DEVEL) console.log('popping from stack')
            if (this.stack.length > 0) {
              this.memDial[this.memIndex] = this.stack.pop()
              stack = [...this.stack]
              MEM_DATA_OUT = [...this.memDial]
            }
          
        }
        inputStack(){
          if(DEVEL) console.log('inputting stack')
          let input = null
          while(input == null || isNaN(Number(input))) {
            input = prompt('input a number')
          }
          if(input == null) return
          this.stack.push(Number(input))
          stack = [...this.stack]
        }
        outputStack(){
          if(DEVEL) console.log('outputting stack')
          //TODO: check if output should be nums or text
          if (false){
              for(let char of this.stack) {
              console.log(String(char));
            }
          }else{
            for(let char of this.stack) {
              console.log(char)
              output.push(char)
            }
            output = output;
          }
        }
        clr(){
          if(DEVEL) console.log('clearing')
          this.stack = []
          stack = [...this.stack]
        }
        compAB(){
          return
        }
        sumAB(){
          if(DEVEL) console.log('adding a and b')
          this.stack.push(this.memDial[this.a] + this.memDial[this.b])
          stack = [...this.stack]
        }
        startWhile(){
          if(DEVEL) console.log('start while')
          this.currentMemWatchCell = this.memIndex
        }
        endWhile(){
          if(this.program == null) return
          let program = this.program.slice(0, this.progIndex)
          let programList:string[] = program.split("")
          console.log('end while')
          programList = programList.reverse()
          let opIndex = this.opIndex
          if (this.currentMemWatchCell == null) return;
          if(this.memDial[this.currentMemWatchCell] > 0) {
            let cycles = 0
            for(let letter of programList) {
              cycles +=1
              if(letter != '!') {
                opIndex -= this.rotateOpAmt
                if(opIndex < 0) {
                  opIndex = this.opDial.length -1
                } else if(opIndex >= this.opDial.length) {
                  opIndex = 0
                }
              } else if(letter == '!') {
                if(this.opDial[opIndex] == this.startWhile) {
                  //console.log('LOOP FROM: ' + (this.program.length - cycles - 1))
                  this.opIndex = opIndex
                  this.progIndex = this.program.length - cycles - 1
                  setOpRoation = opIndex;
                  break
                }
              }
            }
          }
        }
        //test
        reset(){
          this.memDial = [...this.originMemDial]
          MEM_DATA_OUT = [...this.originMemDial]
          resetWheels = true
    
          this.stack = []
          stack = []
          output = []
          this.memIndex = this.startMemIndex
          this.opIndex = this.startOpIndex    
          this.progIndex = 0
          this.program = ''
        }
        printData(){
          console.log(`\t\tMemory Dial: ${this.memDial},\n\t\tMemory Index:${this.memIndex},\n\t\tOperation Index: ${this.opIndex},\n\t\tStack: ${this.stack}.`)
        }
        acceptInput(i:nullString=null){
          if(i == null) {
            var x:nullString = prompt('!/?: ')
          } else {
            var x:nullString = i
          }
    
          if (x == null) return;
    
          if(x == '!') {
            this.opDial[this.opIndex].call(this)
            activeCommand = this.opDial[this.opIndex].name + '()'
          } else {
            this.rotateOp.call(this)
          }
        }
        async acceptString(x:nullString){
          if(x == null) return;
          this.program = x
          while(this.progIndex < x.length) {
            //console.log(D.memDial)
            this.acceptInput(x[this.progIndex])
            if(SLEEPTIME > 0) await sleep();
    
            this.progIndex += 1
            MEM_DATA_OUT = this.memDial;
            }
          if(DEVEL)console.log('Program Complete');
        }
      }
    
    let stack = [];
    let output = [];
    let resetWheels = false;
    let setRotation = false;
    let setOpRoation = false;
    let MEM_DATA_OUT = [0, 0, 0]
    let activeCommand = null
    
    const D = new discoids(0, 0, [0,0,0], 1, 1)
</script>

<div>
  <Wheel reset={() => {D.reset.call(D)}} test={test} bind:rotate={setOpRoation} bind:sliceNames={D.opDialNames}  bind:active={activeCommand} bind:SLEEPTIME={SLEEPTIME}/>
  <MemWheel bind:rotate={setRotation} bind:data={MEM_DATA_OUT} bind:reset={resetWheels} />
  <div class="stacks">
    <div class="stack">
      <table>
        <tr>
          <th><h3>Stack</h3></th>
        </tr>
          {#each stack.reverse() as item}
              <tr><td>{item}</td></tr>
          {/each}
      </table>
  </div>
  <div class="stack">
      <table>
        <tr>
          <th><h3>Output</h3></th>
        </tr>
          {#each output as item}
              <tr><td>{item}</td></tr>
          {/each}
      </table>
  </div>
</div>
  
</div>
<style>
  .stacks{
    display: inline-block;
    width: 100%;
  }
  .stack{
    display: inline-block;
    width: 30%;
    margin: 0 1%;
    vertical-align: top;
  }
  th{
    text-align: center;
    border: 2px solid black;
    padding: 2px 20px;

  }
  h3{
    margin: 0;
  }
  td{
    text-align: center;
    border: 1px solid black;
  }
  table, th, td {
  border-collapse: collapse;
}
</style>