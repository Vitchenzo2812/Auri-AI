/* eslint-disable @typescript-eslint/no-explicit-any */
import { SVGMotionProps } from 'framer-motion'
import { CSSProperties } from 'react'
import * as S from './styles'

export interface BaseAnimationIconProps extends SVGMotionProps<SVGSVGElement> {
  propsPath?: SVGMotionProps<SVGPathElement>
}

export interface BaseIconProps {
  color?: string
  width?: string
  height?: string
  clickeable?: boolean
  children?: any
  className?: string
  viewbox?: string
  colorIcon?: string
  onClick?: (...params: any) => any
  style?: CSSProperties
}

interface Props {
  [key: string]: any
}

const BaseIcon = ({ children, ...props }: Props) => {
  return (
    <S.Icon 
      {...(props || { })} 
      clickeable={String(props.clickeable)} 
      style={props.style} 
      className={props.className} 
      onClick={props.onClick}
    >
      {children}
    </S.Icon>
  )
}

export default BaseIcon
