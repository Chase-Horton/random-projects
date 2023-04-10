<script lang="ts">
    const DEVEL = true;
    const ROTATION = true;
    let SLEEPTIME = 25;
    function sleep() {
        return new Promise(resolve => setTimeout(resolve, SLEEPTIME));
    }
    import MemTableWheel from './wheels/memTableWheel.svelte';
    import TableWheel from './wheels/tableWheel.svelte';
    
    function test(){
      D.acceptString(bangProgram)
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
        this.opDial = [this.increment, this.push, this.inputMem, this.startWhile, this.sumAB, this.outputTop, this.shift, this.decrement, this.endWhile, this.forget, this.pop, this.clr, this.inputStack];
        this.numOfMemDials = memDial.length;
        this.memDial = memDial;
        this.originMemDial = [...memDial];
        this.memIndex = startMemIndex;
        this.startMemIndex = startMemIndex;
        this.opIndex = startOpIndex;
        this.startOpIndex = startOpIndex;
        this.currentMemWatchCell = null;
        this.rotateMemAmt = rotateMemAmt;
        this.rotateOpAmt = rotateOpAmt;
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
            console.log('rotating op dial')
          this.opIndex += this.rotateOpAmt
          if(this.opIndex >= this.opDial.length) {
            this.opIndex = 0
          } else if(this.opIndex < 0) {
            this.opIndex = this.opDial.length -1
          }
          setOpRotation = -1;
        }
        //operations
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
          this.stack.push(this.memDial[this.memIndex])
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
        shift(){
          if(DEVEL) console.log('shifting')
          this.stack.shift()
          stack = [...this.stack]
        }
        forget(){
            if(DEVEL) console.log('forgetting')
            this.stack = this.stack.slice(0, this.stack.length - 1)
            stack = [...this.stack]
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
        inputMem(){
          if(DEVEL) console.log('inputting memory')
          let input = null
          while(input == null || isNaN(Number(input))) {
            input = prompt('input a number')
          }
          if(input == null) return
          this.memDial[this.memIndex] = Number(input)
          MEM_DATA_OUT = [...this.memDial]
        }
        outputTop(){
          if(DEVEL) console.log('outputting top')
          output.push(this.stack[this.stack.length-1])
          output = output;
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
          this.stack.push(this.stack[this.stack.length-1] + this.stack[this.stack.length-2])
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
                  setOpRotation = opIndex;
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
          
          setRotation = this.startMemIndex
          setOpRotation = this.startOpIndex
    
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
            activeCommand = this.opIndex
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
            MEM_DATA_OUT = [...this.memDial];
            }
          if(DEVEL)console.log('Program Complete');
        }
    }
    function getInputType(x:string){
        let out = 'bang'
        for(let char of x) {
            if(char != "!" && char != "?") {
                out = 'text'
                break
            }
        }
        if(out == 'text' && !isNaN(Number(x))){
            out = 'binary'
            for(let char of x){
                if(char != '0' && char != '1'){
                    out = 'number'
                    break
                }
            }
        }
        return out
    }
    function convertToBinary(x:string){
      let binary = '1'
      for(let char of x) {
        if(char == "!") binary += '1'
        else if(char == "?") binary += '0'
      }
      return binary
    }
    function convertToBase(decimal:number, base:number){
        let out = []
        let remainder = decimal
        while(remainder > 0) {
            out.unshift(remainder % base)
            remainder = Math.floor(remainder / base)
        }
        let outStr = ''
        if(base > 10){
            for(let i = 0; i < out.length; i++) {
                out[i] = String.fromCharCode(out[i])
                outStr += out[i]
            }
        } else if(base == 10)
            outStr = convertDecToChars(decimal)
        else{
            outStr = out.join('')
        }
        return outStr
    }
    function convertDecToChars(decimal:number){
        let out = ''
        let remainder = decimal
        while(remainder > 0) {
            out = String.fromCharCode(remainder % 256) + out
            remainder = Math.floor(remainder / 256)
        }
        return out
    }
    function convertDecCharsToDec(x:string){
        let out = 0
        let xList = x.split('')
        for(let i = 0; i < xList.length; i++) {
            console.log(xList[i].charCodeAt(0))
            out += xList[i].charCodeAt(0) * Math.pow(256, xList.length - i - 1)
        }
        return out
    }
    function convertBaseToDec(base:number, baseNum:string){
        let out = 0
        let baseNumList = baseNum.split('')
        for(let i = 0; i < baseNumList.length; i++) {
            if(base > 10) {
                baseNumList[i] = baseNumList[i].charCodeAt(0)
            }
            out += (baseNumList[i]) * Math.pow(base, baseNumList.length - i - 1)
        }
        return out
    }
    function convertToBangs(x:string){
        let out = ''
        for(let char of x) {
            if(char == '1') out += '!'
            else if(char == '0') out += '?'
        }
        out = out.slice(1)
        return out
    }
    function generateFunctionsStr(bangs:string, startIndex:number){
        let out = []
        let opDial = D.opDial
        let currentIndex = startIndex
        let bangList = bangs.split('')
        for(let i = 0; i < bangList.length; i++) {
            if(bangList[i] == '!') {
                out.push(opDial[currentIndex].name)
            } else if(bangList[i] == '?') {
                currentIndex = (currentIndex + 1) % opDial.length
            }
        }
        return out
    }

    let stack = [];
    let output = [];
    let setRotation = null;
    let setOpRotation = null;
    let activeCommand = null;

    let INPUT = '!?!!?!?!?!?!?!?!?!'
    let programType;
    let bangProgram;
    let binaryProgram;
    let decimalProgram;
    let base12Mprogram;
    let base10Program;
    let functionString;
    let base = 65536;

    $:{
        programType = getInputType(INPUT)
        if(programType == 'bang'){
            bangProgram = INPUT
            binaryProgram = convertToBinary(INPUT)
            decimalProgram = parseInt(binaryProgram, 2)
            base12Mprogram = convertToBase(decimalProgram, base)
            if(base == 10)
                base10Program = convertDecCharsToDec(base12Mprogram)
            else
                base10Program = convertBaseToDec(base, base12Mprogram)
        }
        else if (programType == 'binary'){
            binaryProgram = '1' + INPUT
            decimalProgram = parseInt(binaryProgram, 2)
            base12Mprogram = convertToBase(decimalProgram, base)
            if(base == 10)
                base10Program = convertDecCharsToDec(base12Mprogram)
            else
                base10Program = convertBaseToDec(base, base12Mprogram)
        }
        else if (programType == 'number'){
            base10Program = INPUT
            decimalProgram = Number(base10Program)
            binaryProgram = decimalProgram.toString(2)
            bangProgram = convertToBangs(binaryProgram)
            base12Mprogram = convertToBase(decimalProgram, base)
        }
        else if (programType == 'text'){
            base12Mprogram = INPUT
            if(base == 10)
                decimalProgram = convertDecCharsToDec(base12Mprogram)
            else
                decimalProgram = convertBaseToDec(base, base12Mprogram)
            base10Program = decimalProgram
            binaryProgram = decimalProgram.toString(2)
            bangProgram = convertToBangs(binaryProgram)
        }
        functionString = generateFunctionsStr(bangProgram, 0)
    }

    const D = new discoids(0, 0, [0], 1, 1)
    let MEM_DATA_OUT = [...D.memDial]
</script>

<div class="pageContainer">
    <div style="display:flex">
        <div class="stripContainer">
            <TableWheel test={test} bind:rotate={setOpRotation} bind:sliceNames={D.opDialNames} bind:active={activeCommand}  bind:SLEEPTIME={SLEEPTIME}/>
            <MemTableWheel bind:rotate={setRotation} bind:data={MEM_DATA_OUT} labels={['X']}/>
        </div>
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
    <div class="form__group field">
        <input type="input" class="form__field" placeholder="Name" name="name" id='name' bind:value={INPUT} />
        <label for="name" class="form__label">Code</label>
        <p class="form__text">input type: {programType}</p>
        <table>
            <tr>
                <th>Bang</th>
                <td>{bangProgram}</td>
            </tr>
            <tr>
                <th>Binary</th>
                <td>{binaryProgram}</td>
            </tr>
            <tr>
                <th>Decimal</th>
                <td>{decimalProgram.toLocaleString("en-us")}</td>
            </tr>
            <tr>
                <th>Bytes</th>
                <td>{binaryProgram.length/8}</td>
            </tr>
            <tr>
                <th>Base 1.2M</th>
                <td>{base12Mprogram}</td>
            </tr>
            <tr>
                <th>Base 10</th>
                <td>{base10Program}</td>
            </tr>
            <tr>
                <th>Bin</th>
                <td>{convertToBase(base10Program, 2)}</td>
            </tr>
            <tr>
                <th>reconverted</th>
                <td>{convertToBangs(convertToBase(base10Program, 2))}</td>
            </tr>
        </table>
        <table style="margin-top:30px">
            <th colspan="2">Functions</th>
            {#each functionString as func, i}
                <tr>
                    <th>{i}</th>
                    <td class="functions">{func}</td>
                </tr>
            {/each}
        </table>
      </div>
    <div class="btns">
        <button on:click={()=>test()}>Test</button>
        <button on:click={() => D.reset.call(D)}>Reset</button>
    </div>

</div>

<style lang="scss">
    .functions{
        color: darkblue;
        padding: 3px 10px;
    }
    .btns{
        display: flex;
        justify-content: center;
        width: 25%;
        gap: 30px;
        margin-top:30px;
    }
    .stacks{
        display: flex;
        width: 50%;
    }
    .stack{
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
    .pageContainer{
        width: 100%;
        display: inline-block;
        margin-top: 1.3%;
        margin-left: 1.3%;
    }
    .stripContainer{
        width: 50%;
        display: flex;
        justify-items: stretch;
        justify-content: space-evenly;
    }
    button{
        margin: 0px 0px;
        background: #c27028;
	    border: 0;
        border-radius: 3px;
	    padding: 15px 50px;
	    color: white;
        box-shadow: inset 0 -3px #a3540e;
    }
    button:hover{
        cursor: pointer;
    }
    button:active{
        background: #a3540e;
        box-shadow: none;
        transform: translateY(3px);
    }
$primary: #75c293;
$secondary: #38ef7d;
$white: #fff;
$gray: black;
.form__group {
  position: relative;
  padding: 15px 0 0;
  margin-top: 60px;
  width: 30%;
}
.form__text {
    font-size: 1.05rem;
    color: $gray;
    top: 0;
    display: block;
    transition: 0.2s;
}
.form__field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 2px solid $gray;
  outline: 0;
  font-size: 1.3rem;
  color: black;
  padding: 7px 0;
  background: transparent;
  transition: border-color 0.2s;

  &::placeholder {
    color: transparent;
  }

  &:placeholder-shown ~ .form__label {
    font-size: 1.3rem;
    cursor: text;
    top: 20px;
  }
}

.form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: $gray;
}

.form__field:focus {
  ~ .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 1rem;
    color: $primary;
    font-weight:500;    
  }
  padding-bottom: 6px;  
  font-weight: 500;
  border-width: 2px;
  border-image: linear-gradient(to right, $primary,$secondary);
  border-image-slice: 1;
}
/* reset input */
.form__field{
  &:required,&:invalid { box-shadow:none; }
}
    
</style>