'use client'
import { useEffect, useState } from 'react'
type Item = { id:string; sku:string; name:string; unit:string; cost:number; price:number; reorder_level:number }
export default function InventoryPage(){
  const [items,setItems] = useState<Item[]>([])
  const [loading,setLoading] = useState(true)
  useEffect(()=>{
    setItems([
      {id:'1',sku:'SKU-001',name:'AA Batteries 4-Pack',unit:'pack',cost:20,price:35,reorder_level:10}
    ])
    setLoading(false)
  },[])
  return (
    <div>
      <h1>المخزون</h1>
      {loading? <p>جارٍ التحميل...</p> : (
        <table border={1} cellPadding={6}>
          <thead><tr><th>SKU</th><th>الاسم</th><th>الوحدة</th><th>التكلفة</th><th>السعر</th><th>حد إعادة الطلب</th></tr></thead>
          <tbody>
            {items.map(x=>(
              <tr key={x.id}><td>{x.sku}</td><td>{x.name}</td><td>{x.unit}</td><td>{x.cost}</td><td>{x.price}</td><td>{x.reorder_level}</td></tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}