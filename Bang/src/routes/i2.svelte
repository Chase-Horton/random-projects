<script>
    const DEVEL = true;
    const ROTATION = true;
    const SLEEPTIME = 0;
    function sleep() {
        return new Promise(resolve => setTimeout(resolve, SLEEPTIME));
    }
    import Wheel from './wheels/wheel.svelte'
    import MemWheel from './wheels/memWheel.svelte'
    let wheel, color;
    let stack = [];
    let output = [];
    let setRotation = false;
    let data = [0, 0, 0]
    function test(){
      D.acceptString('!!?!??????????!!????????!????????!')
    }
    let discoids = {
      opDial:[this.increment, this.rotateMem, this.decrement, this.push, this.pop, this.outputStack, this.clr, this.compAB, this.sumAB, this.startWhile, this.endWhile],
      numOfMemDials:3,
      memDial:new Array(3).fill(0),
      stack:[],
      memIndex: 0,
      opIndex:0,
      startMemIndex:0,
      startOpIndex:0,
      currentMemWatchCell:null,
    
      rotateMemAmt: 1,
      rotateOpAmt: 1,
      a:0,
      b:0,
    
      progIndex:0,
        getMem: function(){
          return this.memDial[this.memIndex]
        },
        getOp:function(){
          return this.opDial[this.opIndex]
        },
        rotateOp:function(){
          this.opIndex += this.rotateOpAmt
          if(this.opIndex >= this.opDial.length) {
            this.opIndex = 0
          } else if(this.opIndex < 0) {
            this.opIndex = this.opDial.length -1
          }
          if(ROTATION) console.log('rotating op dial: ' + this.opDial[this.opIndex].name)
        },
        //operations
        rotateMem(){
          if(DEVEL) console.log('rotating memory dial')
          this.memIndex += this.rotateMemAmt
          if(this.memIndex >= this.memDial.length) {
            this.memIndex = 0
          } else if(this.memIndex < 0) {
            this.memIndex = this.memDial.length -1
          }
        }
        increment(){
          if(DEVEL) console.log('incrementing')
          this.memDial[this.memIndex] += 1
        }
        decrement(){
          if(DEVEL) console.log('decrementing')
          this.memDial[this.memIndex] -= 1
        }
        push(){
          if(DEVEL) console.log('pushing to stack')
          this.stack.push(this.getMem())
        }
        pop(){
          if(DEVEL) console.log('popping from stack')
          this.memDial[this.memIndex] = this.stack.pop()
        }
        outputStack(){
          if(DEVEL) console.log('outputting stack')
          for(let char of this.stack) {
            console.log(String(char));
          }
          console.log('')
        }
        clr(){
          if(DEVEL) console.log('clearing')
          this.stack = []
        }
        compAB(){
          pass
        }
        sumAB(){
          if(DEVEL) console.log('adding a and b')
          this.stack.push(this.memDial[this.a] + this.memDial[this.b])
        }
        startWhile(){
          if(DEVEL) console.log('start while')
          this.currentMemWatchCell = this.memIndex
        }
        endWhile(){
          let program = this.program.slice(0, this.progIndex)
          program = program.split("")
          console.log('end while')
          program = program.reverse()
          let opIndex = this.opIndex
          if(this.memDial[this.currentMemWatchCell] > 0) {
            let cycles = 0
            for(let letter of program) {
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
                  this.progIndex = this.program.length - cycles -1
                  break
                }
              }
            }
          }
        }
        //test
        reset(){
          this.memDial = new Array(this.numOfMemDials).fill(0)
          this.stack = []
          this.memIndex = this.startMemIndex
          this.opIndex = this.startOpIndex    
          this.progIndex = 0
          this.program = null
        }
        printData(){
          console.log(`\t\tMemory Dial: ${this.memDial},\n\t\tMemory Index:${this.memIndex},\n\t\tOperation Index: ${this.opIndex},\n\t\tStack: ${this.stack}.`)
        }
        acceptInput(i=null){
          if(i == null) {
            var x = prompt('!/?: ')
          } else {
            var x = i
          }
          if(x == '!') {
            this.opDial[this.opIndex]()
          } else {
            this.rotateOp()
          }
        }
        async acceptString(x){
          this.program = x
          while(this.progIndex < x.length) {
            this.acceptInput(x[this.progIndex])
            if(SLEEPTIME > 0) await sleep();
            this.progIndex += 1
            }
            data = this.memDial;
          if(DEVEL)console.log('Program Complete');
        }
      }
    const D = new discoids(3, 0, 0, 1, 1, 0, 1)
    
    
    </script>
    <div>
      <Wheel reset={D.reset} bind:wheel={wheel} test={test} bind:color={color}/>
      <MemWheel bind:rotate={setRotation} bind:data={data}/>
      <div class="stack">
          <h3>Stack</h3>
          <ul>
              {#each stack as item}
                  <li>{item}</li>
              {/each}
          </ul>
      </div>
      <div class="stack">
          <h3>Output</h3>
          <ul>
              {#each output as item}
                  <li>{item}</li>
              {/each}
          </ul>
      </div>
    </div>